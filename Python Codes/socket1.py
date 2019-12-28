#code works 2 different board.
import socket
#first socket created
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="192.168.2.4"
port =6896
s.connect((host,port))

#second socket created
s2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host2 ="192.168.2.5"
port2 =6897
s2.connect((host2,port2))
#functions for measuring the sensors (wemos)
def ts(str):
   s.send('w'.encode())
   data = ''
   data = s.recv(2048).decode()
   print("Water Sensor Value : ","<",data,">")
#data=''
def tss(str):
   s.send('f'.encode())
   data1 = ''
   data1 = s.recv(2048).decode()
   print("Flame Sensor Value : ","<",data1,">")
   #1 its okey there is not flame in environment
#data1 = ''
#functions for measuring the sensors (node)
def tsss(str):
   s2.send('a'.encode())
   data2 = ''
   data2 = s2.recv(2048).decode()
   print("CO Sensor Value : ","<",data2,">")
#data2=''
#our main loop
while 2:
   r = input('Enter to measure values:')
   ts(s)
   tss(s)
   tsss(s)
#closing sockets
s.close ()
s2.close()

