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
pip install rpi_ws281x twisted
cd led\apps\server
python proxy.py

----------- virtual test server on client side --------
This is for testing without real LEDs

Start virtual server (LED display simulator):
cd led\apps\simulator
python simulator.py
