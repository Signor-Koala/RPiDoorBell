from picamera import PiCamera
import time

camera = PiCamera()
imgname = "i0.jpg"
videoname = "v0.h264"
camera.resolution = (640,480)
    
camera.start_preview()
camera.capture(imgname)
camera.start_recording(videoname)
camera.wait_recording(10)
camera.stop_recording()
camera.stop_preview()
