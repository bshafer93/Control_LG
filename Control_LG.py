import os

class LGC7:

    def __init__(self):
            print('ini Cec')

    def ON(self):
            self.Send_Cmd('echo on 0 | cec-client -s -d 1')
            #Discrete on
    def OFF(self):
            self.Send_Cmd('echo standby 0 | cec-client -s -d 1')
            #Discrete off
    def PowerStatus(self):
            self.Send_Cmd('echo pow 0 | cec-client -s -d 1')
            #Discrete off
    ### Query COMMANDS    
    def Send_Cmd(self,cmd):
            os.system(cmd)

