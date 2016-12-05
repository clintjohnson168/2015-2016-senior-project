'''
This file is used to create a video stream object and stream it to a HTML page.
'''

#import libraries
from SimpleCV import *
import time
import os
import webbrowser 

'''
Main fuction to initalize and run the video stream.
'''
def main():
    try:
        #create camara object with streamer
        camera = Camera(0, {"width": 320, "height": 240})   #used to pass into take picture
        stream = JpegStreamer()
        myUrl = stream.url()

        #open the web browser with url
        webbrowser.open(myUrl)

        #run stream for a set amount of time using framecount 
        framecount = 0
        while framecount < 100:
            try:
                camera.getImage().save(stream)
            except Exception as e:
                print(e.message)
                pass
            finally: 
                framecount = framecount + 1
                time.sleep(0.1)
    except Exception as e:
        print(e.message)
        pass
    finally:
        del camera
main()
