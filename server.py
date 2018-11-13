from socket import *
from time import *

host = str(input('host:: '))
port = int(input('port:: '))

#host = '127.0.0.10'
#port = 12345

clients = []

socket_server = socket(AF_INET, SOCK_DGRAM, 0)
socket_server.bind((host, port))

print('\n[Server started on ' + host + ':' + str(port) + ' :: ' + strftime('%H:%M:%S-%d.%m.%Y') + ']\n')
while True:
	try:
		data, address = socket_server.recvfrom(1024)

		if (address not in clients):
			clients.append(address)

		print('[' + strftime('%H:%M:%S-%d.%m.%Y') + ' :: ' + str(address[0]) + ' :: id' + str(address[1]) + ' :: ' + data.decode('utf-8') + ']')

		for client in clients:
			if (data != client):
				socket_server.sendto(data, client)
	except:
		print('\n\n[Server stopped :: ' + strftime('%H:%M:%S-%d.%m.%Y') + ']')
		break

socket_server.close()