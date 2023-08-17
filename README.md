# virtualcom
create virtual comports and send data through them and display the data in the terminal 

### Specs

- Language - Python
- Tool used for creating virtual comports - socat (macOS)
- Library for serial communication - pyserial 

### Steps to run 

1. Run this command in the terminal
```
socat -d -d pty,raw,echo=0 pty,raw,echo=0
```

2. Open a new terminal window and navigate the directory where the scripts are located and run this command
```
python3 sender.py
```

3. Open a new terminal window and navigate the directory where the scripts are located and run this command
```
python3 receiver.py
```

#### Code and Terminal Screenshots 

<img width="1512" alt="Screenshot 2023-08-17 at 11 35 06 PM" src="https://github.com/arpitingle/virtualcom/assets/37828045/25dadacc-8c55-4db8-b9fe-09e45e2150f1">


   
