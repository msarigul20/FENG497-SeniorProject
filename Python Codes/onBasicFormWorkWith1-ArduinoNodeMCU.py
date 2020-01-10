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
   print("GAS Sensor Value : ","<",data,">")
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
   print("WAter Sensor Value : ","<",data2,">")
   data2Int =int(data2);
   if data2Int < 100:
      print("There is NO water in environment.")
   elif data2Int < 200 :
      print("There is little water in environment.")
   elif data2Int < 400 :
      print("There is water be carefull.")
   elif data2Int <1024:
      print("There is DANGER.Solve water problem for sensor healthy.")

def openLamp(str):
   s2.send('x'.encode())
   data4 = ''
   data4 = s2.recv(2048).decode()
   print("sensor value of lamp: ",data4)
def closeLamp(str):

   s2.send('z'.encode())

   data4 = ''

   data4 = s2.recv(2048).decode()

   print("sensor value of lamp: ",data4)


#data2=''

#our main loop
while 2:
   print("*********************************")
   r = input('Enter to measure values:')
   ts(s)
   tss(s)
   tsss(s)
   if r ==  "ON":

      openLamp(s)

   if r == "OFF":
      closeLamp(s)



#closing sockets
s.close ()
s2.close()
