import numpy as np
import cv2
def zero_channel(image, channel):
    im=image.copy()#Creating new array
    im[:,:,channel]=0
    return im

def draw_solid_square_slow(image, x, y, l, color):
    
    color = np.array([color[0],color[1],color[2]])
    #Since it must be done by loops ,then we will loop over all pixels in certain area
    new = np.zeros(np.shape(image),dtype=np.uint8)
    for i in range(len(image)):
        for j in range(len(image[0])):
            new[i,j,0]=image[i,j,0]
            new[i,j,1]=image[i,j,1]
            new[i,j,2]=image[i,j,2]
            
    for i in range (x,x+l+1):#Each matrix
        if i == x or i == x+l:#Upper line or lower line
            for j in range (y,y+l+1):#Each row
                new[i][j]=color
        else:#Side lines
            new[i][y]=color
            new[i][y+l]=color
            
    return new

#Slow took time of 4.21 s

def draw_solid_square_fast(image, x, y, l, color):
    new = image.copy()
    new[x:x+l+1 ,[y,y+l]]=color
    new[[x,x+l+1] ,y:y+l+1]=color
    return new 
#Fast took time 1.42 s

def combine_images_h(img1, img2):
#We will add horzintally so we must check whether they have different rows or not

    row1=np.shape(img1)[0]
    row2=np.shape(img2)[0]

    if row1 > row2 :#Add to image2
        zeros=np.zeros((row1-row2,np.shape(img2)[1],3),dtype=np.uint8)
        img2 = np.concatenate(img2,zeros)

    elif row2 >row1:
        zeros=np.zeros((row2-row1,np.shape(img1)[1],3),dtype=np.uint8)
        img1 = np.vstack((img1,zeros))
    #Now concatenate

    return np.hstack((img1,img2))

def combine_images_v(img1, img2):
    
    shape1=np.shape(img1)
    shape2=np.shape(img2)
    
    if shape1[1] > shape2[1] :#Add to mat2
        zeros = np.zeros((shape1[1]-shape2[1],3),dtype = np.uint8)
        newIm=np.zeros((shape2[0],shape1[1],3),dtype = np.uint8)#New image of matrices of first im and rows of second
        for i in range(len(img2)):        
            newIm[i , :shape2[1]] = img2[i]
        return np.vstack((img1,newIm))
    
    elif shape2[1] > shape1[1]:
        zeros = np.zeros((shape2[1]-shape1[1],3),dtype = np.uint8)
        newIm=np.zeros((shape1[0],shape2[1],3),dtype = np.uint8)#New image of matrices of first im and rows of second
        for i in range(len(img1)):        
            newIm[i , :shape1[1]] = img1[i]
        return np.vstack((newIm,img2))
    
    return np.vstack((img1,img2))


def my_bgr2gray(image):

    im=image.copy()
    for i in range(len(im)):
        for j in range(len(im[0])):
            result=np.sum(im[i,j])//3 #Integer division (average)
            im[i,j]=np.full(3,result,dtype=np.uint8)#3 equal number
    return im

def normalize_img(image):
    means=np.zeros(3)
    stds = np.zeros(3)
    for c in range(3):
        means[c] = np.mean(image[:,:,c])
        stds[c]=np.std(image[:,:,c])
    normal =image.copy()
    normal = (image - means)/stds
    return normal
            
            
            


