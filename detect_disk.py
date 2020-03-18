import os
import time

def main():
 print("Enter any key to continue")
 input()
 loading_points=0
 count=1
 while loading_points!=30:
     backspace=loading_points+7
     print("loading"+"."*loading_points,end='')
     time.sleep(0.1)
     print('\b' * backspace,end='',flush=True)
     loading_points+=1
 if not os.path.exists("/dev/sdb"):
    print("You have no plugged-in usb device")
    exit()
 else:
    while True:
       if os.path.exists("/dev/sdb"+str(count)):
           count+=1
       else:
         break
 print("You have "+str(count-1)+" plugged-in usb device(s)")   
if __name__=='__main__':
 main()
