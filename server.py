#!/usr/bin/python          

import socket               # Import socket module

class nmea_server:
	def send_data_to_port(self,data):
		s = socket.socket()         # Create a socket object
		host = socket.gethostname() # Get local machine name
		port = 12345                # Reserve a port for your service.
		s.bind((host, port))        # Bind to the port
		s.listen(5)                 # Now wait for client connection.
		while True:
		   c, addr = s.accept()     # Establish connection with client.
		   print 'Got connection from', addr
		   c.send(data)
		   c.close()                # Close the connection
	def get_data(self):
		nmea_txt="nmea.txt"
		nmea_data=open(nmea_txt,"r")
		data=nmea_data.read()
		return data

ns=nmea_server()
dt=ns.get_data()
ns.send_data_to_port(dt)
