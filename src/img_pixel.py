#coding；utf-8
import cv2
import numpy as np


def print_pixel_values(img):
    print('img[0:100,0:100]',img[0:100,0:100])
    px = img[100,100]
    print('img[100,100] pixel values bgr',px)
    #blue = img[100,100,0]
    blue = img.item(100,100,0)#快
    print('img[100,100] pixel values of blue',blue)
    green = img[100,100,1]
    print('img[100,100] pixel values of green',green)
    red = img[100,100,2]
    print('img[100,100] pixel values of red',red)
    cv2.imshow('orgimg',img)
    if cv2.waitKey(0) == 27 :
        cv2.destroyWindow(orgimg)

def change_pixel_values(img):
    px = img[10,10]
    print('img [10,10] pixel values bgr',px)
    red = img.item(10,10,2)
    print('img[100,100] pixel values of red',red)
    img.itemset((10,10,2),100)
    print('img set red 100',img.item(10,10,2))
    img.itemset((10,10,0),100)
    img.itemset((10,10,1),100)
    print('img set bgr 100',img[10,10])
    img[20:90,20:90] = [0,0,0]
    cv2.imshow('chaimgblack',img)
    img[20:90,20:90] = [255,0,0]
    cv2.imshow('chaimgred',img)
    img[20:90,20:90] = [0,0,255]
    cv2.imshow('chaimgblue',img)
    img[:,:,2] = 0
    cv2.imshow("allred = 0",img)
    img[:,:,1] = 0
    img[:,:,0] = 0
    cv2.imshow("all = 0",img)

    if cv2.waitKey(0) == 27 :
        cv2.destroyAllWindows()
  

def add_img():
    # Load two images
    img1 = cv2.imread('/home/ly/opencvtest/opencvlearn/image/back.jpg')
    img1 = cv2.resize(img1,None,fx = 1,fy = 2)
    #img2 = cv2.imread('/home/zk/opencvtest/opencvlearn/image/opencvlogo.png')
    img2 = cv2.imread('/home/ly/opencvtest/opencvlearn/image/mianju.jpg')
    img2 = cv2.resize(img2,None,fx = 0.5,fy = 0.5)
    #print(img2)
    # I want to put logo on top-left corner, So I create a ROI
    rows,cols,channels = img2.shape
    print('img2.shape',img2.shape)
    print('img.size',img2.size)
    print('img.dtype',img.dtype)
    roi = img1[50:rows+50, 50:cols+50 ]
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    print('img2gray,shape',img2gray.shape)
    #ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)#大于10的设置为0(黑色），小于设置为255
    ret, mask = cv2.threshold(img2gray, 120, 255, cv2.THRESH_BINARY)#大于10的设置为0(黑色），小于设置为255
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg,img2_fg)
    print('dst.shape',dst.shape)
    img1[50:rows+50, 50:cols+50 ] = dst
    cv2.imshow('res',img1)

    cv2.imshow('img1_bg',img1_bg)
    cv2.imshow('img2_fg',img2_fg)
    cv2.imshow('img2',img2)
    #cv2.imshow('dst',dst)
    #cv2.imshow('img2',img2)
    #cv2.imshow('mask',mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    img = cv2.imread("/home/ly/opencvtest/opencvlearn/image/green.jpg")
    #print_pixel_values(img)
    #change_pixel_values(img)
    add_img()
