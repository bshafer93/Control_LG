import serial 

class LGC7:

    def __init__(self,BD_PORT,BD_BAUDRATE):
        self.BD_PORT = BD_PORT
        self.BD_BAUDRATE = BD_BAUDRATE

    def ON(self):
            self.Send_Cmd('ka 00 01')
            #Discrete on
    def OFF(self):
            self.Send_Cmd('ka 00 00')
            #Discrete off
    def PowerStatus(self):
            self.Send_Cmd('ka 00 FF')
            #Discrete off
    ### Query COMMANDS    
    def Send_Cmd(self,cmd):
        ser = serial.Serial(self.BD_PORT,timeout = 2,bytesize=EIGHTBITS,parity=PARITY_NONE,stopbits=STOPBITS_ONE )
       
        ser.baudrate = self.BD_BAUDRATE
        ser.bau
        full_cmd = bytes(cmd + "\n",'utf-8')
        print(full_cmd)
        ser.write(full_cmd)
        self.Receive_Data(ser)

    def Receive_Data(self,ser):
        data = ser.read(4608)
        print ("received message:", data.decode('unicode-escape'))
        ser.close()

