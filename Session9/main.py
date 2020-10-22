
# importing the module 
import cv2 
import numpy as np
from operations import * 
import matplotlib.pyplot as plt

def region_grow(imgPath ,threshold):

    def getBounds (img, seed : tuple , threshold):
        #Seed is a coordinate lets say img[ y ,x]
        queue = [] #Neighbors
        bounds = [] #All bounds to be colored
        newImg = img.copy()
        
        #Now we add the  8 neigbors
        queue , bounds = lookForNeighbors(img , seed , threshold , queue , bounds)
        ###Now we begin
        iteration = 0
        while len(queue) and iteration < 10000:
            point = queue[0]##Pops first element
            queue.remove(point)
            queue,bounds = lookForNeighbors(img , point , threshold , queue , bounds)
            iteration += 1   

        for  i in bounds:
            xx , yy = i 
            # print(i)
            newImg[yy ,xx] = 0
        
        return newImg                
            
    def click_event(event, x, y, flags, params): 
    
        # checking for left mouse clicks 
        if event == cv2.EVENT_LBUTTONDOWN: 
    
            # displaying the coordinates 
            # on the Shell 
            print(x, ' ', y) 
            new2 = getBounds(cv2.cvtColor(img , cv2.COLOR_BGR2LAB) , (x,y) , threshold)
            cv2.imshow("LAB",cv2.cvtColor(new2 , cv2.COLOR_LAB2BGR))
            cv2.waitKey(0)
            cv2.destroyWindow("LAB")
            
        # reading the image          
    img = cv2.imread(imgPath, 1)
    cv2.imshow('image', img )
    cv2.setMouseCallback("image" , click_event)
    cv2.waitKey(0)   
    cv2.destroyAllWindows()        
    
def global_automatic_threshold(img) : 
    image = img.copy()
    thresh , new = cv2.threshold(img , 0  , 255 , cv2.THRESH_OTSU)
    image = np.zeros_like(new) - image
    thresh2 , x = cv2.threshold(image , thresh  , 255 , cv2.THRESH_OTSU)
    thresh , image = cv2.threshold(image , thresh2-thresh , 255 , cv2.THRESH_BINARY_INV)
    return image
  
            
               
            
          
            