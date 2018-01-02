#coding:utf-8
import cv2
import numpy as np

#dst = a*img1+b*img2 +y
def addimage(img1,img2):
    dst =cv2.addWeighted(img1,0.7,img2,0.3,0)
    cv2.imshow('dst',dst)
    if cv2.waitKey(0) == 27:
        cv2.destroyWindow(dst)

if __name__ =="__main__":
    img1 = cv2.imread("/home/zk/opencvtest/opencvlearn/image/4n.jpg")
    img2 = cv2.imread("/home/zk/opencvtest/opencvlearn/image/n4.png")
    addimage(img1,img2)
