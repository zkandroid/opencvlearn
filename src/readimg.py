#coding:utf-8
import cv2 as cv
import numpy as np

def cvtcolor():
    img = np.zeros((3,3),dtype =np.uint8)
    img1 =cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    print('img and img1')
    print(img)
    print(img1)

if __name__ == '__main__':
    cvtcolor()
    img =cv.imread('image/45.jpg',cv.IMREAD_COLOR)
    #将【20，20】的像素设置为白像素
    img[20,20] =[255,255,255]
    print(img.item(150,120,0))

    img.itemset((150,120,0),255)
    print(img.item(150,120,0))
    #将所有的白像素设置为绿像素
    img[:,:,0] = 1
    cv.imshow('img',img)
    #设定感兴趣区域
    img2 = cv.imread('image/45.jpg')
    print('img2.shape',img2.shape)
    print('img2.size',img2.size)
    print('img2.dtype',img2.dtype)
    my_roi = img2[100:180,100:180]
    img2[10:90,10:90]=my_roi
    cv.imshow('img2',img2)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
