from socket import *
from asyncio import *

class Server(object):

	host = '127.0.0.99'
	port = 12345
	server_socket = None

	def __init__(self, host = host, port = port):
		self.host = host
		self.port = port

	def run_server(self):
		self.server_socket = socket(AF_INET, SOCK_STREAM, 0)
		self.server_socket.bind((self.host, self.port))
		self.server_socket.listen(10)
		self.server_socket.setblocking(False)
		print('[Server started]')

	@coroutine
	async def pass_data(self, loop, client):
		status = True
		while status:
			data = (await loop.sock_recv(client, 255)).decode('utf-8')
			print(data)
			if (data == 'left'):
				status = False
			await loop.sock_sendall(client, message.encode('utf8'))
		client.close()

	@coroutine
	async def accept_client(self, loop):
		while True:
			client, _ = await loop.sock_accept(self.server_socket)
			loop.create_task(self.pass_data(loop, client))

if __name__ == '__main__':
	server = Server()
	server.run_server()

	try:
		server_loop = get_event_loop()
		server_loop.run_until_complete(server.accept_client(server_loop))

	except:
		server_loop.close()
		print('[Server stopped]')

server.server_socket.close()