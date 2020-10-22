import cv2
import numpy as np

def getSquare(img , coord1:tuple , coord2: tuple):
    col1 = np.array(img[coord1[1] , coord1[0]] , dtype = np.int32)
    col2 = np.array(img[coord2[1] , coord2[0]] , dtype = np.int32)
    # print(col1)
    # print(col2)
    # print("Col1 is ",col1)
    dist = 0
    for i in range(3):
        dist += ((col1[i] - col2[i]) ** 2)
    # print(dist ** 0.5)    
    return dist ** 0.5    
    
    
def lookForNeighbors(img ,seed ,threshold, queue , bounds) :
    x , y =seed
    
    #Right
    if x!=len(img[0])-1 :
        point = (x+1 , y)
        dist = getSquare(img , seed , point)
        if dist <= threshold and bounds.count(point) == 0 :#Check that is not calaculated
            queue.append(point)
            bounds.append(point)
        
        
    
    #Upper
    if  y != 0 :
        upperX , upperY =(x , y-1)
        dist  = getSquare(img , (x,y) , (upperX , upperY))
        
        if dist <= threshold and bounds.count((upperX , upperY)) == 0 :
            queue.append((upperX , upperY))
            bounds.append((upperX , upperY))
            
    #Left
    
    if x != 0 : 
        point = (x-1 , y)
        dist = getSquare(img , seed , point)
        if dist <= threshold and bounds.count(point) == 0 :
            queue.append(point)
            bounds.append(point)
    
    #Bottom
    
    if y != (len(img) -1) : 
        point = (x , y+1)
        dist = getSquare(img , seed , point)
        if dist <= threshold and bounds.count(point) == 0 :
            queue.append(point)
            bounds.append(point)
              
    #####Diagonals
    ##Upper right
    
    if x!=len(img[0])-1 and y != 0  :
        point = (x+1 , y-1)
        dist = getSquare(img , seed , point)
        if dist <= threshold and bounds.count(point) == 0 :
            queue.append(point)
            bounds.append(point)
    
    # Upper Left
    if x != 0  and y != 0  :
        point = (x-1 , y-1)
        dist = getSquare(img , seed , point)
        if dist <= threshold and bounds.count(point) == 0 :
            queue.append(point)
            bounds.append(point)
    
    #Bottom left
    if x != 0  and y != (len(img) -1) :
        point = (x-1 , y+1)
        dist = getSquare(img , seed , point)
        if dist <= threshold and bounds.count(point) == 0 :
            queue.append(point)
            bounds.append(point)
            
    #Bottom right
    if x!=len(img[0])-1  and y != (len(img) -1) :
        point = (x+1 , y+1)
        dist = getSquare(img , seed , point)
        if dist <= threshold and bounds.count(point) == 0 :
            queue.append(point)
            bounds.append(point)

                               
    return queue , bounds           


img = cv2.imread("cat.jpg")

# getSquare(img , (100,100) , (150,100))