# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:45:25 2020

@author: Javier Velasquez P.
"""  

import cv2
import numpy as np

#FUNCTIONS

def Cross(a,b):
    n1=np.shape(a)
    n2=np.shape(b)
    matrizr=np.zeros((n1[0],n2[1]))
    for r in list(range(0,n1[0])):
        for c in list(range(0,n2[1])):
            for k in list(range(0,n2[0])):
                matrizr[r,c]+=a[r,k]*b[k,c]
    return matrizr

def fval(m):
    	n=np.shape(m)
    	xm=np.zeros(n) 
    	ym=np.zeros(n)
    	zm=np.zeros(n)
    	for i in list(range(0,n[0])):
    		for j in list(range(0,n[1])):
    			xm[i,j]=i
    			ym[i,j]=j
    			zm[i,j]=m[i,j]
    
    	xm=np.reshape(xm,np.size(xm),order='C')
    	ym=np.reshape(ym,np.size(ym),order='C')
    	zm=np.reshape(zm,np.size(zm),order='C')
    	return xm,ym,zm
    
def func(x0,x,y,p0,p1,p2,p3,p4,p5):
        x1=y
        x2=x
        x3=x*y
        x4=y*y
        x5=x*x
        return p0*x0+(p1*x1)+(p2*x2)+(p3*x3)+(p4*x4)+(p5*x5) 


def dullRazor (image):
    #Gray scale
    grayScale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY )
    #Black hat filter
    kernel = cv2.getStructuringElement(1,(9,9)) 
    blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
    #Gaussian filter
    bhg= cv2.GaussianBlur(blackhat,(3,3),cv2.BORDER_DEFAULT)
    #Binary thresholding (MASK)
    ret,mask = cv2.threshold(bhg,10,255,cv2.THRESH_BINARY)
    #Replace pixels of the mask
    dst = cv2.inpaint(image,mask,6,cv2.INPAINT_TELEA)
    return dst


#IMAGE ACQUISITION

#Input image
path='ISIC_0031023.jpg'

#Read image
image=cv2.imread(path,cv2.IMREAD_COLOR)
#Image cropping
cropped_img=image[30:410,30:560]

#Dullrazor
img = dullRazor(cropped_img)
    
#SHADDING ATENUATION

#Split channels
B,G,R=cv2.split(img)

#Extract pixels from corners
size=np.shape(B)
c1=B[0:20,0:20] #Upper left corner
c2=B[0:20,size[1]-20:size[1]] #Upper right corner
c3=B[size[0]-20:size[0],0:20] #Lower left corner
c4=B[size[0]-20:size[0],size[1]-20:size[1]] #Lower right corner
#Concatenate pixels
c5=np.concatenate((c1, c2), axis=1)
c6=np.concatenate((c3, c4), axis=1)
corners=np.concatenate((c5, c6), axis=0)
        
#Split matrix for normal equation
x,y,z=fval(corners)

x0=np.ones(len(x))
x1=y
x2=x
x3=x*y
x4=y*y
x5=x*x
        
#Vectors normalization
x1=x1/np.amax(x1)
x2=x2/np.amax(x2)
x3=x3/np.amax(x3)
x4=x4/np.amax(x4)
x5=x5/np.amax(x5)
z=z/np.amax(z)
        
#reshape
x0=x0.reshape(len(x0),1)
x1=x1.reshape(len(x1),1)
x2=x2.reshape(len(x2),1)
x3=x3.reshape(len(x3),1)
x4=x4.reshape(len(x4),1)
x5=x5.reshape(len(x5),1)
z=z.reshape(len(z),1)
        
#Concatenate vectors
X=np.concatenate((x0, x1, x2, x3, x4, x5), axis=1)
Y=z
        
#Get parameters (Normal Equation) 
p=Cross((Cross((np.linalg.inv(Cross(X.T,X))),X.T)),Y)
        
#Get inputs of original image (Blue channel)
xv,yv,zv=fval(B)
x0v=np.ones(len(xv))
        
#Normalization of vectors
xv=xv/np.amax(xv)
yv=yv/np.amax(yv)
zv=zv/np.amax(zv)
forma=np.shape(B)
        
#Attenuation of Blue channel
nim=func(x0v,xv,yv,p[0],p[1],p[2],p[3],p[4],p[5])
attenuator=nim.reshape(forma,order='C')
attenuation_img=(B/attenuator)/np.amax(B)
    
#Display images
cv2.imshow("Original image",image)
cv2.imshow("Cropped image",cropped_img)
cv2.imshow("Blue channel",B)
cv2.imshow("Attenuator element",attenuator)
cv2.imshow("Shadding attenuation ",attenuation_img)

cv2.waitKey()
cv2.destroyAllWindows()