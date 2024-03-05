import machine
import time

switch = machine.Pin(0, machine.Pin.IN)
led = machine.Pin(2, machine.Pin.OUT)

def callback(Pin):
    led.value(not led.value())
    
    
switch.irq(trigger = machine.Pin.IRQ_FALLING, handler = callback)
