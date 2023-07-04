import os
import signal
import time
import multiprocessing
import RPi.GPIO as GPIO
from datetime import datetime

#Setting GPIO pins for input
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#Defining the running of the various other scripts that make up the project
def webstreamStart():
    print("stream starting")
    os.system("python3 \"/home/pi/DoorBellScripts/DbPi_stream.py\"")
    print("stream end")

def captureStart():
    print("capture starting")
    os.system("python3 \"/home/pi/DoorBellScripts/DbPi_capture.py\"")
    print("capture end")

def emailStart():
    print("email starting")
    os.system("python3 \"/home/pi/DoorBellScripts/DbPi_email.py\"")
    print("email end")
   
#Definition of the Archiving process that stores the image and video files created in a folder
def Archival():
    date = datetime.now().strftime("%Y%m%d%H:%M:%S")
    imgname = "i"+str(date)+".jpg"
    videoname = "v"+str(date)+".h264"
    os.system("mv \"/home/pi/i0.jpg\" \"/home/pi/Archives/"+imgname+"\"")
    print("image moved")
    os.system("mv \"/home/pi/v0.h264\" \"/home/pi/Archives/"+videoname+"\"")
    print("video moved")

#Starting of the program in a loop
while(True):
    print ("Starting...")

    
    #Defining the different scripts to run under multiprocessing processes
    processStream = multiprocessing.Process(target = webstreamStart)
    processCapture = multiprocessing.Process(target = captureStart)
    processEmail = multiprocessing.Process(target = emailStart)
    processArchive = multiprocessing.Process(target = Archival)
   
    processStream.start()
    
    
    GPIO.wait_for_edge(7,GPIO.RISING)
    
    #Code to be executed after the button is pressed

    #This code kills the stream process to allow the other scripts to use the camera
    for line in os.popen("ps ax | grep "+"DbPi_stream.py"+" | grep -v grep"):
        fields = line.split()
        pid = fields[0]
        os.kill(int(pid), signal.SIGKILL)

    processStream.join()
    
    processCapture.start()
    
    time.sleep(1.5)
    
    processEmail.start()
    
    processCapture.join()
    
    try:
        processEmail.join()
    except:
        print("Email has already been sent")

    processArchive.start()
    processArchive.join()
    

