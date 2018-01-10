#coding:utf-8
import cv2
import numpy as np

#dst = a*img1+b*img2 +y
def addimage(img1,img2):
    dst =cv2.addWeighted(img1,0.7,img2,0.3,0)
    cv2.imshow('dst',dst)
    if cv2.waitKey(0) == 27:
        cv2.destroyWindow(dst)

def add_img_mask(img,mask):
	print(mask.shape[0])
	mask_low = mask.shape[0]
	mask_row =mask.shape[1]
	dst = cv2.add(img[0:mask_low,0:mask_row],mask)
	#dst = cv2.add(img,mask)
	img[0:mask_low,0:mask_row] = dst
	return img

def addweighted_img_mask(img,mask,img_value,mask_value,r):
	print(mask.shape[0])
	mask_low = mask.shape[0]
	mask_row =mask.shape[1]
	dst = cv2.addWeighted(img[0:mask_low,0:mask_row],img_value,mask,mask_value,r)
	#dst = cv2.add(img,mask)
	img[0:mask_low,0:mask_row] = dst
	return img
if __name__ =="__main__":
	img1 = cv2.imread("/home/ly/opencvtest/opencvlearn/image/4n.jpg")
	img2 = cv2.imread("/home/ly/opencvtest/opencvlearn/image/n4.png")
	logo = cv2.imread("/home/ly/opencvtest/opencvlearn/image/opencvlogo.png")
	mianju = cv2.imread("/home/ly/opencvtest/opencvlearn/image/mianju.jpg")
	mianju = cv2.resize(mianju,(200,200))
	#addimage(img1,img2)
	dst_mask =add_img_mask(img1,logo)
	#dst_mianju =add_img_mask(img1,mianju)
	#cv2.imshow('dst_mianju',dst_mianju)
	cv2.imshow('dst_mask',dst_mask)
	dst_addweighted = addweighted_img_mask(img1,logo,0.3,0.7,0)
	cv2.imshow('dst_addweighted',dst_addweighted)
	if cv2.waitKey(0) == 27:
		cv2.destoryWindow(dst_mask)
		cv2.destoryWindow(dst_addweighted)
	
	
