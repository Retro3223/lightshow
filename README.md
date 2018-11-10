Based on https://github.com/tinue/APA102_Pi

# Prerequisites

see above, but basically

* pi should have raspbian 9 on it

* pi should have SPI enabled

```
raspi-config

# Interfacing Options > SPI

reboot
```

* Adafruit_Python_GPIO should be installed 

see https://github.com/adafruit/Adafruit_Python_GPIO, but basically

```
apt-get install build-essential python3-pip python3-dev python3-smbus git
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
python setup.py install
```

for testing on a not-raspberry pi this seemed to work:
```
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
python setup.py install
```


# Deploy

```
python deploy.sh
```

will push code and restart the script. To make it run on boot up, you will have to run

```
systemctl enable lightshow.service
```

manually on the pi
