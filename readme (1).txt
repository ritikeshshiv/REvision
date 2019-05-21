INSTALLING THE RPLCD LIBRARY
The RPLCD library can be installed from the Python Package Index, or PIP. It might already be installed on your Pi, but if not, enter this at the command prompt to install it:

sudo apt-get install python-pip

After you get PIP installed, install the RPLCD library by entering:

sudo pip3 install RPLCD

The example programs below use the Raspberry Pi’s physical pin numbers, not the BCM or GPIO numbers. I’m assuming you have your LCD connected the way it is in the diagrams above, but I’ll show you how to change the pin connections if you need to.