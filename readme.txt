download and install Microsoft Visual C++ Compiler for Python 2.7:
https://aka.ms/vcpython27

---------- client side ------------
For the client app the following packages are needed:
pip install kivy pillow twisted numpy

For kivy GUI framework in general the following packags are needed:
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

Start client app:
cd led
python main.py
in the GUI navigate to 'Panel Settings' and hit 'connect'

-----------server side------------
sudo pip install rpi_ws281x twisted
cd led\apps\server
sudo python proxy.py

----------- virtual test server on client side --------
This is for testing without real LEDs

Start virtual server (LED display simulator):
cd led\apps\simulator
python simulator.py

---------- create a deamon service launching at system start-up --------------
sudo apt-get install daemontools daemontools-run
- create service named 'led'
sudo mkdir /etc/service/led
- make start-up script called 'run'
sudo nano /etc/service/led/run
- type
#!/bin/bash
exec sudo /usr/bin/python /home/pi/led_remote_display/led/apps/server/proxy.py
- set permissions
sudo chmod u+x /etc/service/led/run
- check status
sudo svstat /etc/service/led
- kill
sudo svc -k /etc/service/led
- start
sudo svc -u /etc/service/led
