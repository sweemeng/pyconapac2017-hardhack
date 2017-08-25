import urequests
import network
from machine import Pin
from machine import I2C
import ssd1306


def main():
    i2c = I2C(sda=Pin(4), scl=Pin(5))
    display = ssd1306.SSD1306_I2C(128, 64, i2c, 60)   
    
    sta_if = network.WLAN(network.STA_IF)

    if sta_if.isconnected():
        
        config = sta_if.ifconfig()
        private_ip = config[0]
        r = urequests.get('http://httpbin.org/get')
        print(r.json())
        data = r.json()
        public_ip = data["origin"]
    else:
        private_ip = ""
        public = ""

    display.fill(0)
    display.show()

    display.text("Private IP: ", 6, 5)
    display.text(private_ip, 12, 15)
    display.text("Public IP: ", 6, 25)
    display.text(public_ip, 12, 35)
    display.show()
   

if __name__ == "__main__":
    main()
    
