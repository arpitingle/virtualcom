import serial
import time

sender_port = '/dev/ttys001' 
baud_rate = 9600

with serial.Serial(sender_port, baud_rate, timeout=1) as ser:
    while True:
        ser.write(b'Hello from sender!\n')
        ser.flush()
        time.sleep(2)  # Send data every two seconds
