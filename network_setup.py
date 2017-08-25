import network
import time

def setup():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('ACCESS_POINT','PASSWD')
    while not sta_if.isconnected():
        pass
    print(sta_if.ifconfig())

if __name__ == "__main__":
    setup()
