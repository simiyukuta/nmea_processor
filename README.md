NMEA PROCESSOR
  REQUIREMENTS
  python 2.7.3
  pynmea 0.6 (https://pypi.python.org/pypi/pynmea)
  
  
SERVER.PY sends nmea sentences to port 12345 on the local machine
CLIENT.PY Receives the data,looks for the GPGGA and gives the description of each GPGGA sentence
nmea.txt sample nmea data that we send to port 12345
receiver.txt a file created for temporarily storing the nmea sentences
How TO RUN ON LINUX MACHINE
open the terminal 
change directory to where the files are probably cd ../../nmea_processor
Run these commands:
  python server.py &
  python client.py
