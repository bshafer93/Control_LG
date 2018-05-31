import serial 

class LGC7:

    def __init__(self,BD_PORT,BD_BAUDRATE):
        self.BD_PORT = BD_PORT
        self.BD_BAUDRATE = BD_BAUDRATE

    def ON(self):
            self.Send_Cmd('ka 0 1')
            #Discrete on
    def OFF(self):
            self.Send_Cmd('ka 00 00')
            #Discrete off

    ### Query COMMANDS    
    def Send_Cmd(self,cmd):
        ser = serial.Serial(self.BD_PORT,timeout = 3 )
       
        ser.baudrate = self.BD_BAUDRATE
        full_cmd = bytes(cmd + "\r",'utf-8')
        ser.write(b'ka 00 01\r')
        self.Receive_Data(ser)

    def Receive_Data(self,ser):
<<<<<<< HEAD
        data = ser.read(4096)
=======
        data = ser.read(10)
>>>>>>> parent of f8c2e31... 1
        print ("received message:", data)
        ser.close()




