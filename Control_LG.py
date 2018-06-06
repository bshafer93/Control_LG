import os
import subprocess
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
          process =  subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
          stdout = process.communicate()[0]
          print ('STDOUT:{}'.format(stdout))

