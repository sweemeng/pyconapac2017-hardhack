from machine import Pin
from machine import I2C
import dht
import ssd1306
import utime

def main():
    i2c = I2C(sda=Pin(4), scl=Pin(5))
    display = ssd1306.SSD1306_I2C(128, 64, i2c, 60)
    sensor = dht.DHT22(Pin(13))

    while True:
        display.fill(0)
        display.show()
        sensor.measure()
        temperature = "Temp : %s" % sensor.temperature()
        humidity    = "Humid: %s" % sensor.humidity()
        display.text(temperature, 6, 15)
        display.text(humidity, 6, 25)
        display.show()
        utime.sleep(30)

if __name__ == "__main__":
    main()
