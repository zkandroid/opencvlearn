#coding:utf-8
import cv2
import numpy as np

def start(img):
	kernel =np.ones((5,5),np.float32)/25
	img = cv2.resize(img,(500,500))
	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	lower_blue=np.array([40,43,46])
	upper_blue=np.array([110,255,255])
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	print('mask',mask)
	print('kernel',kernel)
	#2D卷积
	#filter2d = cv2.filter2D(mask,-1,kernel)
	filter2d = cv2.filter2D(img,-1,kernel)
	#平均
	#blur = cv2.blur(mask,(3,5))#模板大小3*5
	blur = cv2.blur(img,(3,5))#模板大小3*5
	#高斯模糊
	#Gaussianblur = cv2.GaussianBlur(mask,(5,5),0)
	Gaussianblur = cv2.GaussianBlur(img,(5,5),0)
	#中值模糊
	#meidianblur = cv2.medianBlur(mask,5)
	meidianblur = cv2.medianBlur(img,5)
	#.双边滤波
	#bilateralFilter = cv2.bilateralFilter(mask,9,75,75)
	bilateralFilter = cv2.bilateralFilter(img,9,75,75)

                #腐蚀膨胀
	#erode=cv2.erode(mask,None,iterations=1)
	erode=cv2.erode(mask,None,iterations=1)
                #cv2.imshow('erode',erode)
	dilate=cv2.dilate(erode,None,iterations=1)
                #cv2.imshow('dilate',dilate)
	#开运算，先腐蚀在膨胀
	#opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
	opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

	#闭运算，先膨胀再腐蚀
	#closeing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
	closeing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
	#.形态学梯度,其实就是一幅图像膨胀与腐蚀的差别。
	#gradient = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
	gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
	#礼帽 原始图像与进行开运算之后得到的图像的差。
	#tophat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)
	tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
	#黑帽，进行闭运算之后得到的图像与原始图像的差
	#blackhat = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)
	blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

	cv2.imshow('mask',mask)
	cv2.imshow('filter2d',filter2d)
	cv2.imshow('blur',blur)
	cv2.imshow(' meidianblur', meidianblur)
	cv2.imshow('Gaussianblur',Gaussianblur)
	cv2.imshow('bilateralFilter',bilateralFilter)
	cv2.imshow('erode',erode)
	cv2.imshow('dilate',dilate)
	cv2.imshow('opening',opening)
	cv2.imshow('closeing',closeing)
	cv2.imshow('gradient',gradient)
	cv2.imshow('tophat',tophat)
	cv2.imshow('blackhat',blackhat)
	cv2.imshow('img',img)
	if cv2.waitKey(0) == 27 :
		cv2.destroyAllWindows()
	







if __name__ == '__main__':
	img_start = cv2.imread('/home/ly/opencvtest/opencvlearn/image/zaosheng.jpg')
	start(img_start)
