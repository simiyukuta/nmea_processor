<p>NMEA PROCESSOR</p><br>
<p><b>Python code to send NMEA sentences to a port,receive them,parse them and print out the output on the terminal</b></p> 
  REQUIREMENTS<br>
  python 2.7.3<br>
  pynmea 0.6 (https://pypi.python.org/pypi/pynmea)<br>
  AUTHOR: KUTA JAMES SIMIYU <br>
  AUTHOR PROFILE:http://aiti.mit.edu/accounts/237/<br>

  
<b><u>How TO RUN ON LINUX MACHINE</u></b>
<p>open the terminal<p> 
<p>change directory to where the files are probably cd ../../nmea_processor</p>
<p>Run these commands:</p>
 <p><i> python server.py &</i></p>
  <p><i>python client.py </i><p>
  
  <p><b>NOTE</b></p>
  <p>To stop the server,kill it with the pid generated</p>
  <p>FILE DESCRIPTION</p>
  
<p><b>SERVER.PY</b> - sends nmea sentences to port 12345 on the local machine</p>
<p><b>CLIENT.PY</b> - Receives the data,looks for the GPGGA and gives the description of each GPGGA sentence</p>
<p><b>nmea.txt sample nmea data that we send to port 12345
<p><b>receiver.txt</b> - a file created for temporarily storing the nmea sentences</p>
