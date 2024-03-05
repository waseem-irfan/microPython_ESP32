import machine

sw1 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
sw2 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
dr1 = machine.Pin(22, machine.Pin.OUT)
dr2 = machine.Pin(23, machine.Pin.OUT)

press = False
irq_pin = 0

def handle_interrupt(pin):
    global press
    press = True
    global irq_pin
    irq_pin = int(str(pin)[4:-1])

sw1.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)
sw2.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)

while True:
    if press:
        print(irq_pin)
        press = False
        
        if irq_pin == 15:
            dr1.value(0)
            dr2.value(1)
            print('counter')
        elif irq_pin == 21:
            dr1.value(1)
            dr2.value(0)
            print('clockwise')
        else:
            pass