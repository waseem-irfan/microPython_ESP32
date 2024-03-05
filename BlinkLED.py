import machine
import time

led = machine.Pin(2, machine.Pin.OUT)
def blink_led_ntime(num, on_time,off_time,msg):
    count = 0
    while (count < num):
        led.on()
        time.sleep(on_time)
        led.off()
        time.sleep(off_time)
        count+=1
    print(msg)
