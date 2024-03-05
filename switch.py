import machine
import time

led = machine.Pin(2,machine.Pin.OUT)
switch = machine.Pin(0,machine.Pin.IN)

def blink_led_ntimes(num,on_time,off_time,msg):
    counter = 0
    while (counter < num):
        led.on()
        time.sleep(on_time)
        led.off()
        time.sleep(off_time)
        counter += 1
    print(msg)
    

while True:
    if(switch.value() == 0):
        blink_led_ntimes(5,0.2,0.4,"Blink is Done!")
        
