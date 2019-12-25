import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="192.168.2.4"
port =6896
s.connect((host,port))

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

#data = ''
while 2:
   r = input('enter')
   ts(s)
   tss(s)
s.close ()