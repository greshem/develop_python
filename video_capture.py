import VideoCapture

cam = VideoCapture.Device(devnum=0)
#cam.displayPropertyPage() ## deprecated
#cam.displayCaptureFilterProperties()
#cam.displayCapturePinProperties()
#cam.setResolution(960, 720)
#cam.setResolution(768, 576) ## PAL
#cam.setResolution(352, 288) ## CIF
import time;
def get_cur_time():
    return time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
	
cur_time=get_cur_time();
cam.saveSnapshot("%s.jpg"%cur_time, quality=75, timestamp=3, boldfont=1)
