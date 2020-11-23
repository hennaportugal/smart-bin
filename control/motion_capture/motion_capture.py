#!/usr/bin/python

# original script by brainflakes, improved by pageauc, peewee2 and Kesthal
# www.raspberrypi.org/phpBB3/viewtopic.php?f=43&t=45235

# You need to install PIL to run this script
# type "sudo apt-get install python-imaging-tk" in an terminal window to do this

import io
import subprocess
import os
import time
from datetime import datetime
from PIL import Image

class MotionCapture():
    def __init__(self):
        # Motion detection settings:
        # Threshold          - how much a pixel has to change by to be marked as "changed"
        # Sensitivity        - how many changed pixels before capturing an image, needs to be higher if noisy view
        # ForceCapture       - whether to force an image to be captured every self.forceCaptureTime seconds, values True or False
        # self.filepath           - location of folder to save photos
        # self.filenamePrefix     - string that prefixes the file name for easier identification of files.
        # self.diskSpaceToReserve - Delete oldest images to avoid filling disk. How much byte to keep free on disk.
        # self.cameraSettings     - "" = no extra settings; "-hf" = Set horizontal flip of image; "-vf" = Set vertical flip; "-hf -vf" = both horizontal and vertical flip
        self.threshold = 100
        self.sensitivity = 0.8
        self.forceCapture = False
        self.forceCaptureTime = 60 * 60 # Once an hour
        self.filepath = "/home/pi/darkflow-master/test_data"
        self.filenamePrefix = "capture"
        self.diskSpaceToReserve = 40 * 1024 * 1024 # Keep 40 mb free on disk
        self.cameraSettings = ""

        # settings of the photos to save
        self.saveWidth   = 1296
        self.saveHeight  = 972
        self.saveQuality = 15 # Set jpeg quality (0 to 100)

        # Test-Image settings
        self.testWidth = 25
        self.testHeight = 85

        # this is the default setting, if the whole image should be scanned for changed pixel
        self.testAreaCount = 1
        self.testBorders = [ [[1,self.testWidth],[1,self.testHeight]] ]  # [ [[start pixel on left side,end pixel on right side],[start pixel on top side,stop pixel on bottom side]] ]
        # self.testBorders are NOT zero-based, the first pixel is 1 and the last pixel is testWith or self.testHeight

        # with "self.testBorders", you can define areas, where the script should scan for changed pixel
        # for example, if your picture looks like this:
        #
        #     ....XXXX
        #     ........
        #     ........
        #
        # "." is a street or a house, "X" are trees which move arround like crazy when the wind is blowing
        # because of the wind in the trees, there will be taken photos all the time. to prevent this, your setting might look like this:

        # self.testAreaCount = 2
        # self.testBorders = [ [[1,50],[1,75]], [[51,100],[26,75]] ] # area y=1 to 25 not scanned in x=51 to 100

        # even more complex example
        # self.testAreaCount = 4
        # self.testBorders = [ [[1,39],[1,75]], [[40,67],[43,75]], [[68,85],[48,75]], [[86,100],[41,75]] ]

        # in debug mode, a file debug.bmp is written to disk with marked changed pixel an with marked border of scan-area
        # debug mode should only be turned on while testing the parameters above
        self.debugMode = False # False or True

    # Capture a small test image (for motion detection)
    def captureTestImage(self, settings, width, height):
        command = "raspistill %s -w %s -h %s -t 200 -e bmp -n -o -" % (settings, width, height)
        imageData = io.BytesIO()
        imageData.write(subprocess.check_output(command, shell=True))
        imageData.seek(0)
        im = Image.open(imageData)
        buffer = im.load()
        imageData.close()
        return im, buffer

    # Save a full size image to disk
    def saveImage(self, settings, width, height, quality, diskSpaceToReserve):
        self.keepDiskSpaceFree(self.diskSpaceToReserve)
        #time.sleep(1)
        timenow = datetime.now()
        filename = self.filepath + "/" + self.filenamePrefix + "-%04d%02d%02d-%02d%02d%02d.jpg" % (timenow.year, timenow.month, timenow.day, timenow.hour, timenow.minute, timenow.second)
        subprocess.call("raspistill %s -w %s -h %s -t 200 -e jpg -q %s -n -o %s" % (settings, width, height, quality, filename), shell=True)
        print ("Captured %s" % filename)

    # Keep free space above given level
    def keepDiskSpaceFree(self, bytesToReserve):
        if (self.getFreeSpace() < bytesToReserve):
            for filename in sorted(os.listdir(self.filepath + "/")):
                if filename.startswith(self.filenamePrefix) and filename.endswith(".jpg"):
                    os.remove(self.filepath + "/" + filename)
                    print ("Deleted %s/%s to avoid filling disk" % (self.filepath,filename))
                    if (self.getFreeSpace() > bytesToReserve):
                        return

    # Get available disk space
    def getFreeSpace(self):
        st = os.statvfs(self.filepath + "/")
        du = st.f_bavail * st.f_frsize
        return du

    def run(self):
        # Get first image
        print("motion_capture:: run")
        image1, buffer1 = self.captureTestImage(self.cameraSettings, self.testWidth, self.testHeight)

        # Reset last capture time
        lastCapture = time.time()

        while (True):

            # Get comparison image
            image2, buffer2 = self.captureTestImage(self.cameraSettings, self.testWidth, self.testHeight)

            # Count changed pixels
            changedPixels = 0
            takePicture = False

            if (self.debugMode): # in debug mode, save a bitmap-file with marked changed pixels and with visible testarea-borders
                debugimage = Image.new("RGB",(self.testWidth, self.testHeight))
                debugim = debugimage.load()

            for z in range(0, self.testAreaCount): # = xrange(0,1) with default-values = z will only have the value of 0 = only one scan-area = whole picture
                for x in range(self.testBorders[z][0][0]-1, self.testBorders[z][0][1]): # = xrange(0,100) with default-values
                    for y in range(self.testBorders[z][1][0]-1, self.testBorders[z][1][1]):   # = xrange(0,75) with default-values; self.testBorders are NOT zero-based, buffer1[x,y] are zero-based (0,0 is top left of image, self.testWidth-1,self.testHeight-1 is botton right)
                        if (self.debugMode):
                            debugim[x,y] = buffer2[x,y]
                            if ((x == self.testBorders[z][0][0]-1) or (x == self.testBorders[z][0][1]-1) or (y == self.testBorders[z][1][0]-1) or (y == self.testBorders[z][1][1]-1)):
                                # print "Border %s %s" % (x,y)
                                debugim[x,y] = (0, 0, 255) # in debug mode, mark all border pixel to blue
                        # Just check green channel as it's the highest quality channel
                        pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])
                        if pixdiff > self.threshold:
                            changedPixels += 1
                            if (self.debugMode):
                                debugim[x,y] = (0, 255, 0) # in debug mode, mark all changed pixel to green
                        # Save an image if pixels changed
                        if (changedPixels > self.sensitivity):
                            # ~ time.sleep(1)
                            takePicture = True # will shoot the photo later
                        if ((self.debugMode == False) and (changedPixels > self.sensitivity)):
                            break  # break the y loop
                    if ((self.debugMode == False) and (changedPixels > self.sensitivity)):
                        break  # break the x loop
                if ((self.debugMode == False) and (changedPixels > self.sensitivity)):
                    break  # break the z loop

            if (self.debugMode):
                debugimage.save(self.filepath + "/debug.bmp") # save debug image as bmp
                print ("debug.bmp saved, %s changed pixel" % changedPixels)
            # else:
            #     print "%s changed pixel" % changedPixels

            # Check force capture
            if self.forceCapture:
                if time.time() - lastCapture > self.forceCaptureTime:
                    takePicture = True

            if takePicture:
                time.sleep(1)
                lastCapture = time.time()
                self.saveImage(self.cameraSettings, self.saveWidth, self.saveHeight, self.saveQuality, self.diskSpaceToReserve)
                print('saved picture')
                break

            # Swap comparison buffers
            image1 = image2
            buffer1 = buffer2
