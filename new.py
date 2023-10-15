import cv2
import cvlib as cv
import numpy as np
import urllib.request
import pyttsx3
from cvlib.object_detection import draw_bbox
 
url='http://192.168.249.236/cam-hi.jpg'
im=None
 
def speak(text):
    # Create a pyttsx3 object
    engine = pyttsx3.init()
    
    # Set voice properties
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # You can change the index to change the voice

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()
 
def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
 
        cv2.imshow('live transmission',im)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
            
    cv2.destroyAllWindows()
        
def run2():
    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
 
        bbox, label, conf = cv.detect_common_objects(im)
        im = draw_bbox(im, bbox, label, conf)
 
        # Speak out the labels
        for l in label:
            speak(l)
 
        cv2.imshow('detection',im)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
            
    cv2.destroyAllWindows()
 
 
 
if __name__ == '__main__':
    print("started")
    run2() 
    # with concurrent.futures.ProcessPoolExecutor() as executer:
            # f1= executer.submit(run1)
            # f2= executer.submit(run2)
