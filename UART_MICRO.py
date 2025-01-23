import machine
import sys
import select

#pins = [machine.Pin(i,machine.Pin.OUT) for i in range(2,10)]
uart =machine.UART(0, baudrate=115200)
uart.init(115200,bits=8, parity=None, stop=1, timeout=3000)

led = machine.Pin(25, machine.Pin.OUT)

def check_input():
    while True:
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            user_input = sys.stdin.read(8)
            if user_input.strip() == "11111111":
                led.value(1)
            else:
                led.value(0)

check_input()
