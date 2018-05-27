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
        full_cmd = bytes(cmd + "\n",'utf-8')
        ser.write(full_cmd)
        self.Receive_Data(ser)

    def Receive_Data(self,ser):
        data = ser.read(4096)
        print ("received message:", data)
        ser.close()


    def power_on(self):
        self.run_command('k', 'a', 1, 1)

    def run_command(self, c1, c2, set_id, data):
        ser = serial.Serial(self.BD_PORT,timeout = 3 )
       
        ser.baudrate = self.BD_BAUDRATE
        ser.write(bytes('%c%c %x %x\n' % (c1, c2, set_id, data), 'utf-8'))