import serial

receiver_port = '/dev/ttys002'  
baud_rate = 9600

with serial.Serial(receiver_port, baud_rate, timeout=1) as ser:
    while True:
        data = ser.readline()
        print("Received:", data.decode().strip())
