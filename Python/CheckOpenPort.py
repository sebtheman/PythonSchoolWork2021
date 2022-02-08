#I am using this Python file to look for open ports on my network for testing LAN multiplayer TicTacToe
#This Python file scans through all ports and stops when it finds one open

import socket, random

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print('Hostname is ' + hostname)
print('Local IP adress is ' + local_ip)

resultOfCheck = None
timesTriedToGetPort = 0
while resultOfCheck != 0:
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_number = random.randint(0, 65535)
    test_location = (local_ip, port_number)
    resultOfCheck = socket_obj.connect_ex(test_location)
    print('Tryed port number ' + str(port_number) + ' and received status ' + str(resultOfCheck))
    timesTriedToGetPort += 1
    if resultOfCheck == 0:
        print('Port ' + str(port_number) + ' is open.')
        print('It took ' + str(timesTriedToGetPort) + ' times to get this port number.')
    socket_obj.close()