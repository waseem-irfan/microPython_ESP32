import machine
import time
import SSD1306

scl = machine.Pin(22, machine.Pin.OUT, machine.Pin.PULL_UP)
sda = machine.Pin(21, machine.Pin.OUT, machine.Pin.PULL_UP)

i2c = machine.I2C(scl=scl, sda = sda, freq = 400000)
oled = SSD1306.SSD1306_I2C(128, 64, i2c, addr = 0x3C)

import dht

d = dht.DHT22(machine.Pin(23))

def display():
    d.measure()
    t = d.temperature()
    h = d.humidity()
    
    oled.fill(0)
    
     # Display the temperature
    oled.text('Temperature *C:', 10, 10)
    oled.text(str(t), 90, 20)
    # Display the humidity
    oled.text('Humidity %:', 10, 40)
    oled.text(str(h), 90, 50)
    # Update the screen display
    oled.show()
    

start = time.ticks_ms()

while True:
    if time.ticks_ms() - start >= 2000:
        display()
        start = time.ticks_ms()
        



