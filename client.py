#!/usr/bin/python           

import socket               # Import socket module
from pynmea.streamer import NMEAStream

class nmea_client:
	def receive_nmea_data(self):
		s = socket.socket()         # Create a socket object
		host = socket.gethostname() # Get local machine name
		port = 12345                # Reserve a port for your service.
		s.connect((host, port))
		resp=s.recv(1024)
		s.close                     # Close the socket when done
		return resp


class nmea_worker:
	def create_nmea_objects(self,data):
		self.store_data_in_file(data)
		nmea_txt = 'receiver.txt'
		with open(nmea_txt, 'r') as data_file:
			nmea_stream=NMEAStream(stream_obj=data_file)
			nmea_data=nmea_stream.get_objects()
			nmea_objects=[]
			while nmea_data:
				nmea_objects+=nmea_data
				nmea_data=nmea_stream.get_objects()
				return nmea_objects
				
	def get_gpgga_attributes(self,nmea_objects):
		for nmea_ob in nmea_objects:
			if nmea_ob.sen_type=='GPGGA':
				print "UTC of Position "+nmea_ob.sen_type
				print "Latitude "+nmea_ob.latitude+" |Latitude direction "+nmea_ob.lat_direction
				print "Longitude "+nmea_ob.longitude+" | Longitude direction " +nmea_ob.lon_direction
				print "GPS quality indicator "+nmea_ob.gps_qual
				print "Number of satellites in use "+nmea_ob.num_sats
				print "Horizontal dilution of position "+nmea_ob.horizontal_dil
				print "Antenna altitude above/below mean sea level "+nmea_ob.antenna_altitude
				print "Meters  (Antenna height unit) "+nmea_ob.altitude_units
				print "Geoidal separation "+nmea_ob.geo_sep
				print "Meters  (Units of geoidal separation) "+nmea_ob.geo_sep_units
				print "Age in seconds since last update from diff. reference station "+nmea_ob.age_gps_data
				print "Differential reference station ID  "+nmea_ob.ref_station_id
				print "Checksum "+nmea_ob.checksum
				print "----------------------------------"
				
	def store_data_in_file(self,data):
		f=open('receiver.txt','w')
		f.write(data)
		f.close()
	
	def clean_receiver(self):
		f=open('receiver.txt','w')
		f.write('')
		f.close()
			
					
nc=nmea_client()
nmea_data=nc.receive_nmea_data()
nw=nmea_worker()
no=nw.create_nmea_objects(nmea_data)
nw.get_gpgga_attributes(no)
