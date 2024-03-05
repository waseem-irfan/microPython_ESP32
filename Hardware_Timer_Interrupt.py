import machine

led = machine.Pin(2, machine.Pin.OUT)

tim0 = machine.Timer(0)

def callback_handle(timer):
    led.value(not led.value())
    

# tim0.init(period = 2000, mode = machine.Timer.ONE_SHOT, callback= lambda t: led.value(not led.value()))

tim0.init(period = 50, mode = machine.Timer.PERIODIC, callback= callback_handle)
