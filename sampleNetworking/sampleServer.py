import socket 

def Main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c, addr = s.accept()
	print("Connecton fromL " + str(addr))
	while True:
		data = c.rev(1024).decode('utf-8')
		if not data:
			break
		print("From connected user: " + data)
		data = data.upper()
		print("Sending: " + data)
		c.send(data.encdoe('utf-8'))

	c.close()

Main() 