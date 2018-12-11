download and install Microsoft Visual C++ Compiler for Python 2.7:
https://aka.ms/vcpython27

For the client app the following packages are needed:
pip install kivy pillow twisted

For kivy GUI framework in general the following packags are needed:
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

Start virtual server (LED display simulator):
cd led\apps\simulator
python simulator.py

Start client app:
cd led
python main.py
in the GUI navigate to 'Panel Settings' and hit 'connect'
