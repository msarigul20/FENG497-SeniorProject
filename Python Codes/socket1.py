#import socket

#socket = socket.socket()

#host = "192.168.2.4"  # ESP IP in local network
#port = 6896  # ESP32 Server Port

#socket.connect((host, port))
#message = "H"
#socket.send(message)

#data = ""

#while len(data) < len(message):
    #data += socket.recv(1)

#print(data)

#socket.close()
"""
import socket

HOST = '192.168.2.4'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'L')
    data = s.recv(1024)

print('Received', repr(data))
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="192.168.2.4"
port =6896
s.connect((host,port))

def ts(str):
   s.send('e'.encode())


   data = ''
   data = s.recv(2048).decode()



   print(data[0:]+"\n")

data=''


while 2:
   r = input('enter')
   ts(s)
s.close ()

#hi world to try
