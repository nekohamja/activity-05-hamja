import cv2 as cv
import numpy as np


img = cv.imread("nicco.jpg")


if(len(img.shape)<2):
    print('\nimage type: Grayscale image')
    exit()
elif len(img.shape)==3:
    print('\nimage type: Colored image')



maxheight = 1920
maxwidth = 1080
minheight =480
minwidth = 360
size = 1500000

print("\nimage dimension limit : max=1920 x 1080 and min = 489 x 360")
imgheight = img.shape[0]
imgwidth = img.shape[1]

print ("current loaded image dimention:",imgheight, "x",imgwidth)
if((imgheight < maxheight and imgheight > minheight) and  (imgwidth < maxwidth and imgwidth > minwidth)):
    print("Current loaded image is within the boundaries!")
else:
    print("Current loaded image is not the boundaries!")

print("\nSet size:",size)
imgsize = img.size
print("current loaded image size:",imgsize)
if(imgsize < size):
    print("current loaded image has lower pixel count than the set image size!")
else:
    print("\ncurrent loaded image has higher pixel count than the set image size!")


print ("\ncurrent loaded image datatype:",img.dtype)


print("\naccess a pixel value using item method")
i,j,k = input("enter row,colum and channel: ").split()
row1,colum1,channel1=[int(i),int(j),int(k)]
res=img.item(row1,colum1,channel1)
print("Result:",res)


print("\nModify a pixel value using item set method")
x,y = input("Enter row and colum: ").split()
blue = int(input("Enter change i blue chanel: "))
green =int(input("Enter change in green channel: "))
red = int(input("Enter change is red channel: "))
print("\nResult")
row2,colum2,=[int(x),int(y)]
img.item(row2,colum2,0)
img.item(row2,colum2,1)
img.item(row2,colum2,2)
res1 = img[row2,colum2]
print("Before:",res1)
img.itemset((row2,colum2,0),blue)
img.itemset((row2,colum2,1),green)
img.itemset((row2,colum2,2),red)
res2 =img[row2,colum2]
print("After:",res2, "\n")
