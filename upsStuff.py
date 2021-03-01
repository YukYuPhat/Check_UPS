#John Schuster
#jschuster@ridedart.com
#going to check the ups and return details needed in a screenshot

#import telnetlib
import telnetlib
#import password file
from passwdStuff import whatPasswd
import time, datetime
import pyautogui


#the ips we are going to use
UPS1 = '10.1.105.19'
UPS2 = '10.1.105.18'
UPS3 = '10.1.105.18'
UPS4 = '10.1.105.18'
UPS5 = '10.1.105.18'
UPS6 = '10.1.105.18'
UPS7 = '10.1.105.18'
UPS8 = '10.1.105.18'

UPSList = [UPS1,UPS2,UPS3,UPS4,UPS5,UPS6];

UPSDict = {UPS1:'DARTCHUPSD2',UPS2:'Platform C',UPS3: 'Platform H',UPS4: 'Platform I',UPS5: 'Platform N',UPS6:'DCSLounge'}
timeStuff = 15

if __name__ == '__main__':
    
    #get the password for the UPS
    upsPassWord = whatPasswd('UPS')
    
#    for ups in range(len(UPSList)):

    #create a file to write text to by date and which UPS
    CurrentDay = time.strftime("%e%b%y%S",time.localtime())
#    ScreenStuff = CurrentDay +UPSDict[UPSList[ups]]+ "_.txt"  
    ScreenStuff = CurrentDay +UPSDict[UPSList[0]]+ ".txt"  
    f = open(ScreenStuff, "a+")

    #make connection
#    tn= Telnet(UPSList[ups])
    tn= telnetlib.Telnet(UPSList[0])
    time.sleep(timeStuff)
    #read until User Name :
    a = tn.read_very_eager()
    print(a.decode('ascii'))
    #write the user name
    tn.write(upsPassWord['User'].encode('ascii') + b"\r\n")
    time.sleep(timeStuff)
    
    #read until password
    a = tn.read_very_eager()
       
    #write the password
    tn.write(upsPassWord['Password'].encode('ascii') + b"\r\n")
    time.sleep(timeStuff)

    #read the intial screen
    a = tn.read_very_eager()
    print(a.decode('ascii'))
    #pass it to the file 
    f.write(a.decode('ascii'))
    #write alarmcount -p all
    time.sleep(timeStuff)

    tn.write(b"alarmcount -p all\r\n")
    #read the warnings
    a = tn.read_very_eager()
    print(a.decode('ascii'))
    #write the warnings to the file

    f.write(a.decode('ascii'))
    time.sleep(timeStuff)


    #write event option
    tn.write(b"eventlog\r\n")
    #read the first page of event file
    a = tn.read_very_eager()
    print(a.decode('ascii'))

    #append that to the file
    f.write(a.decode('ascii'))
    time.sleep(timeStuff)
    #create loop to do the next steps 5 times
    for i in range(5):
    
        #press spacebar using pyautogui to get the page
        tn.write(b' ')
        #append that to the file
        a = tn.read_very_eager()
        print(a.decode('ascii'))
        f.write(a.decode('ascii'))
        time.sleep(timeStuff)
    # if count is completed or break, press ESC
    tn.write(b'\x1b')
    time.sleep(timeStuff)
    #to delete log you must confirm by typing YES
    tn.write(b"exit\r\n")
    time.sleep(timeStuff)
    tn.close()
    f.close()