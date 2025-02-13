from progress.bar import Bar
from progress.counter import Counter
import cv2
import json
import os
import random

class FrameGenerator():
    def __init__(self,filename:str = None) -> None:
        if filename == None:
            filename = input("Filename: ")
        self.FILENAME = filename
        self.save_path = 'First video'
        self.random_NAMES = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z','0','1','2','3','4','5','6','7','8','9',]
    
    def Generate(self,DETAILS:bool = True,is_RandomName:bool = True):

        '''You give this method youre filename
        and this method returns you the frames of
        youre video.'''

        cap = cv2.VideoCapture(self.FILENAME) #Open Video

        CounterBar = Counter('Counting Frames: ') #Create a counter bar for counting frames

        frame_counter = 1

        while(cap.isOpened()):
            ret, frame = cap.read() #Read video frames
            if ret:
                CounterBar.next() #Count in countbar
                frame_counter += 1 #Count in var
            else:
                break
            cv2.waitKey(1)

        CounterBar.finish() #Stop counterbar progress
        cap.release() #Release the video

        del cap #Remove the loaded video var
        cap = cv2.VideoCapture(self.FILENAME) #Create a new load of video

        ProgressBar = Bar('Saving Frames', max=frame_counter-1) #Create a progress bar for see when the progress done
        if not os.path.exists(os.path.join(os.getcwd(),self.save_path)):
            os.makedirs(os.path.join(os.getcwd(),self.save_path))
        frame_counter = 1
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                nm = ""
                for c in range(15):
                    nm += random.choice(self.random_NAMES) #Generate random name
                if is_RandomName:
                    cv2.imwrite(os.path.join(os.getcwd(),self.save_path,"%s.jpg"%nm),frame) #Save frame with random name
                else:
                    cv2.imwrite(os.path.join(os.getcwd(),self.save_path,f"Frame_{str(frame_counter)}.jpg"),frame) #Save frame with choosed name
                ProgressBar.next() #One step forward of progress bar
                frame_counter += 1 #Count again
            else:
                break
            cv2.waitKey(1)
        
        self.CAP = cap
        self.FRAMES = frame_counter

        if DETAILS:
            print(f"\n\n{str(self.FRAMES)} Frame Successfully saved!!!\nSpeed of video: {int(self.CAP.get(cv2.CAP_PROP_FPS))}FPS") #See details of Progress

    def DETAILS(self,filename:str = 'Details.json'):

        '''This method gives you a
        detail of last progress in a json file.'''

        with open(filename,'w') as file:
            json.dump({'Name':self.FILENAME,'Frames':self.FRAMES,'FPS':self.CAP.get(cv2.CAP_PROP_FPS)},file,indent=3) #Save details

