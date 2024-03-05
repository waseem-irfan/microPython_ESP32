import SSD1306
import machine

scl = machine.Pin(22, machine.Pin.OUT, machine.Pin.PULL_UP)
sda = machine.Pin(21, machine.Pin.OUT, machine.Pin.PULL_UP)

i2c = machine.I2C(scl = scl , sda = sda, freq = 400000)

oled = SSD1306.SSD1306_I2C(128, 64, i2c, addr= 0x3C)

def print_txt(msg, x, y , clc):
    if clc:
        oled.fill(0)
    oled.text(msg, x, y)
    oled.show()
    
#def Erase():
#   oled.fill(0)
#   oled.show()
    