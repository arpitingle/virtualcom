# virtualcom
create virtual comports and send data through them and display the data in the terminal 

# Specs

Language - Python
Tool used for creating virtual comports - socat (macOS)
Library for serial communication - pyserial 

# Steps to run 

1. Run this command in the terminal
```
socat -d -d pty,raw,echo=0 pty,raw,echo=0
```

2. Open a new terminal window and naviage the directory where the scripts are located and run this command
```
python3 sender.py
```

3. Open a new terminal window and naviage the directory where the scripts are located and run this command
```
python3 receiver.py
```





   
