# code works 2 different boards which are nodeMCU and WEMOS D1
#last checking on 27.01.2020
import socket  # imported for communication with nodes.

# first socket created for node1 which is WEMOS D1
socket_wemos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_wemos = "192.168.2.4"
port_wemos = 6896
socket_wemos.connect((host_wemos, port_wemos))

# first socket created for node1 which is nodeMCU
socket_nodemcu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_nodemcu = "192.168.2.5"
port_nodemcu = 6897
socket_nodemcu.connect((host_nodemcu, port_nodemcu))


# ***functions for measuring the sensors on WEMOS D1
# Gas calculation function-->
def calculate_gas(str):
    print("*************** GAS SECTION BEGIN ************")
    socket_wemos.send('w'.encode())
    data_gas = ''
    data_gas = socket_wemos.recv(2048).decode()
    print("GAS Sensor Value : ", "<", data_gas, ">")
    # parsing to compare (string to int)
    data_gas_int = int(data_gas)
    if data_gas_int < 300:
        print("---There is NO dangerous gas in environment.")
    elif data_gas_int < 600:
        print("---There is little dangerous gas in environment. Please check the environment.")
    elif data_gas_int < 1024:
        print("---There is DANGER.Immediately must solve gas problem to protect yourself.")
    print("*************** GAS SECTION END ************")
    print(" ")


# Flame calculation function-->
def calculate_flame(str):
    print("*************** FLAME SECTION BEGIN ************")
    socket_wemos.send('f'.encode())
    data_flame = ''
    data_flame = socket_wemos.recv(2048).decode()
    print("Flame Sensor Value : ", "<", data_flame, ">")
    # if value is "1" that means there is not flame in environment otherwise vice versa.
    if data_flame == "1":
        print("---There is NO flame in environment. ")
    else:
        print("---There is flame in environment BE SAFE!")

    print("*************** FLAME SECTION END ************")
    print(" ")


# ***functions for measuring the sensors on nodeMCU

# Water calculation function-->
def calculate_water(str):
    print("*************** WATER SECTION BEGIN ************")
    socket_nodemcu.send('a'.encode())
    data_water = ''
    data_water = socket_nodemcu.recv(2048).decode()
    print("Water Sensor Value : ", "<", data_water, ">")
    # parsing to compare (string to int)
    data_water_int = int(data_water)
    if data_water_int < 100:
        print("---There is NO water in environment.")
    elif data_water_int < 200:
        print("---There is little water in environment.")
    elif data_water_int < 400:
        print("---There is water be careful. Please check the environment.")
    elif data_water_int < 1024:
        print("---There is DANGER.Immediately must solve water problem to protect sensors.")
    print("*************** WATER SECTION END ************")
    print(" ")


# Flame calculation function-->
def calculate_temperature(str):
    print("*************** TEMPERATURE SECTION BEGIN ************")
    print("Please wait 2 seconds for calculations")
    socket_nodemcu.send('d'.encode())
    data_temperature = ''
    data_temperature = socket_nodemcu.recv(2048).decode()
    print("DHT Temperature Sensor Value : ", "<", data_temperature, ">")
    print("*************** TEMPERATURE SECTION END ************")
    print(" ")


# Humidity calculation function-->
def calculate_humidity(str):
    print("*************** HUMIDITY SECTION BEGIN ************")
    print("Please wait 2 seconds for calculations")
    socket_nodemcu.send('h'.encode())
    data_humidity = ''
    data_humidity = socket_nodemcu.recv(2048).decode()
    print("DHT Humidity Sensor Value : ", "<", data_humidity, ">")
    print("*************** HUMIDITY SECTION END ************")
    print(" ")


# Led OPEN Order functions
def open_order_LED(str):
    socket_nodemcu.send('x'.encode())
    data_led_open = ''
    data_led_open = socket_nodemcu.recv(2048).decode()
    print("LED state is : ", data_led_open)


# Led CLOSE Order functions
def close_order_LED(str):
    socket_nodemcu.send('z'.encode())
    data_led_close = ''
    data_led_close = socket_nodemcu.recv(2048).decode()
    print("LED state is :", data_led_close)


# Main Loop waiting ENTER

while 2:
    print("///////////////////////////////////////////////////////")  # for following outputs
    print("To Calculations enter --C--")
    print("To Calculations enter --LC--")
    input_main_menu = input('Enter your input with capital letters : ')
    # temp is temporary string.
    temp = "temp"
    if input_main_menu == "C":
        # doing calculations
        calculate_gas(temp)
        calculate_flame(temp)
        calculate_water(temp)
        calculate_temperature(temp)
        calculate_humidity(temp)

    elif input_main_menu == "LC":
        input_led_control = input('Enter LEDON or LEDOFF to control LED :');
        # if user wants to open led do it.
        if input_led_control == "LEDON":
            open_order_LED(temp)
        # if user wants to close led which is already open do it.
        elif input_led_control == "LEDOFF":
            close_order_LED(temp)
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You enter wrong input for LED controlling menu.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("You enter wrong input for main menu.")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# closing sockets
socket_wemos.close()
socket_nodemcu.close()
