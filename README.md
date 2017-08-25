# Some micropython demo

## Bill of material
![The things](DSC_1203.JPG?raw=True)

* Nodemcu module. It have lua build in, which is cool oh well. I forgot where I get it from
* a ssd1306 Oled module. It is pretty common. I get it here https://www.cytron.com.my/p-ds-oled-mod
* a DHT22. Also a common electronic part. I get it https://www.cytron.com.my/p-sn-dht22

## The code
Here is the some demo code for the micropython demo. Here's how to run it. 

1. Setup all the tools
```
$ pip install -r requiirements.txt
```
2. setup micropython on your esp8266. Look online for this
3. connect your esp8266 dev board
4. Change the `network_setup.py`, `ACCESS_POINT` to your AP, `PASSWD` to password
5. Upload and run
```
$ ampy -b 115200 -p /dev/ttyUSB0 put network_setup.py
$ ampy -b 115200 -p /dev/ttyUSB0 run network_setup.py
```
6. Run the following command to run the demo
```
$ ampy -b 115200 -p /dev/ttyUSB0 put sensor_demo.py
$ ampy -b 115200 -p /dev/ttyUSB0 run sensor_demo.py 
$ ampy -b 115200 -p /dev/ttyUSB0 put public_ip.py
$ ampy -b 115200 -p /dev/ttyUSB0 run public_ip.py
```


