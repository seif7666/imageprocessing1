import numpy as np
import cv2
def zero_channel(image, channel):
    im=image.copy()#Creating new array
    im[:,:,channel]=0
    return im

def draw_solid_square_slow(image, x, y, l, color):
    color = np.array([color[0],color[1],color[2]])
    #Since it must be done by loops ,then we will loop over all pixels in certain area
    new = image.copy()
    
    for i in range (x,x+l+1):#Each matrix
        if i == x or i == x+l:#Upper line or lower line
            for j in range (y,y+l+1):#Each row
                new[i][j]=color
        else:#Side lines
            new[i][y]=color
            new[i][y+l]=color
            
    return new