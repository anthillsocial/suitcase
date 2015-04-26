import serial, time

class MotorController:
    def  __init__(self): 
        usbport = '/dev/ttyAMA0'
        self.ser = serial.Serial(usbport, 57600, timeout=1) # 9600
        self.init_stepper()

    def init_stepper(self):
        self.log('Initi stepper')
        # mSet mode to "Styep Gret Off"
        self.write([0x01, 0x00, 0x08])
        self.write([0x09, 0x00, 0x00, 0x64, 0x00])
        # Set frequency to 1000
        self.write([0x09, 0x00, 0x03, 0xE8, 0x00])
        # Enabel endstops
        self.write([0x02, 0x00, 0x11])
        self.write([0x02, 0x00, 0x13])

    def forward(self):
        self.log('forward')
        self.write([0x08, 0x00, 0xFF, 0x03, 0xE8]) 
        self.write([0x1C, 0x00])

    def reverse(self):
        self.log('reverse')
        self.write([0x08, 0x00, 0x00, 0x03, 0xE8]) # reverse
        self.write([0x1C, 0x00])

    def write(self, binaryArray):
        start = 0xA0        
        end = 0x50
        binaryArray.insert(0, start)
        binaryArray.append(end)
        command = self.to_binary_str(binaryArray) 
        self.ser.write(command)
        self.log('write:{}'.format(command))

    def end(self):
        self.ser.close()
    
    def to_binary_str(self, array):
        return ''.join(chr(b) for b in array)

    def log(self, msg):
        print(msg)

if __name__ == "__main__": 
    stepper = MotorController()
    stepper.forward()
    time.sleep(1)
    stepper.reverse()
    stepper.end()



