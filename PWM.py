import machine

dr1 = machine.Pin(21, machine.Pin.OUT)
dr2 = machine.Pin(19, machine.Pin.OUT)

en1 = machine.Pin(18, machine.Pin.OUT)

pwm = machine.PWM(en1)

def cw():
    dr1.value(1)
    dr2.value(0)

def ccw():
    dr1.value(0)
    dr1.value(1)
    
def start(rotation):
    pwm.init()
    if (rotation == 'cw'):
        cw()
        
    elif (rotation == 'ccw'):
        ccw()
        
        
def stop():
    pwm.deinit()
    dr1.value(0)
    dr2.value(0)
    
    
        
