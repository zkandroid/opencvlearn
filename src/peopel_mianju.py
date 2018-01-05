#coding:utf-8
import cv2
import numpy as np

def add_img(back_img,mianju_img,x,y,w,h):
	# Load two images
	#cv2.imshow('back_img',back_img)
	#back_img = cv2.resize(back_img,None,fx = 2,fy = 2)
	mianju_img = cv2.resize(mianju_img,(w,h))
	# I want to put logo on top-left corner, So I create a ROI
	rows,cols,channels = mianju_img.shape
	#roi = back_img[y:y+rows, x:x+cols]
	roi = back_img[y:y+w, x:x+h]
#	cv2.imshow('roi',roi)
	# Now create a mask of logo and create its inverse mask also
	mianju_imggray = cv2.cvtColor(mianju_img,cv2.COLOR_BGR2GRAY)
	#ret, mask = cv2.threshold(mianju_imggray, 10, 255, cv2.THRESH_BINARY)#大于10的设置为0(黑色），小于设置为255
	ret, mask = cv2.threshold(mianju_imggray, 120, 255, cv2.THRESH_BINARY)#大于10的设置为0(黑色），小于设置为255
	mask_inv = cv2.bitwise_not(mask)
	# Now black-out the area of logo in ROI
	back_img_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
	# Take only region of logo from logo image.
	mianju_img_fg = cv2.bitwise_and(mianju_img,mianju_img,mask = mask)
	# Put logo in ROI and modify the main image
	dst = cv2.add(back_img_bg,mianju_img_fg)
	back_img[y:y+w, x:x+h] = dst
	cv2.imshow('res',back_img)
	#cv2.imshow('back_img_bg',back_img_bg)
	#cv2.imshow('mianju_img_fg',mianju_img_fg)
	#cv2.imshow('dst',dst)
	#cv2.imshow('mianju_img',mianju_img)
	#cv2.imshow('mask',mask)
	#if cv2.waitKey(0) == 27 :
		#cv2.destroyAllWindows()
	#return back_img
#正脸
face_cascade = cv2.CascadeClassifier('/home/ly/opencv/data/haarcascades_cuda/haarcascade_frontalface_default.xml')
#侧脸
#face_cascade = cv2.CascadeClassifier('/home/ly/opencv/data/haarcascades/haarcascade_profileface.xml')
#
#face_cascade = cv2.CascadeClassifier('/home/ly/opencv/data/haarcascades_cuda/haarcascade_frontalface_alt_tree.xml')

#face_cascade = cv2.CascadeClassifier('/home/ly/opencvtest/haar/face_cascades/HS.xml')
eye_cascade = cv2.CascadeClassifier('/home/ly/opencv/data/haarcascades/haarcascade_eye.xml')
def face_eye(mianju_img):
	cap = cv2.VideoCapture(0)
	while(True):
		#获取视频及返回状态
		ret, img = cap.read()
		img = cv2.resize(img,None,fx = 2,fy = 2)
		#将获取的视频转化为灰色
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		#检测视频中的人脸，并用vector保存人脸的坐标、大小（用矩形表示）
		faces = face_cascade.detectMultiScale(gray, 1.3, 4)
		#脸部检测
		for (x,y,w,h) in faces:
			#cv2.rectangle(img,(x+w,y+w),(w,h),(255,0,0),2)
			#cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
			print(x,y,w,h)
			#x为到图片顶部的位置，y为到图片左边的位置，所以上是[y:y+w, x:x+h]，w是人脸正方形的宽，h是长
			mymianju=add_img(img,mianju_img,x,y,w,h)
			#检测视频中脸部的眼睛，并用vector保存眼睛的坐标、大小（用矩形表示）
			eyes = eye_cascade.detectMultiScale(roi_gray,1.3,4)
			#眼睛检测
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		#按q键退出while循环
		#cv2.imshow('img',img)
		if cv2.waitKey(30) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()



if __name__ == "__main__":
	back_img = cv2.imread('/home/ly/opencvtest/opencvlearn/image/back.jpg')
	mianju_img = cv2.imread('/home/ly/opencvtest/opencvlearn/image/mianju.jpg')
	#add_img(back_img,mianju_img)
	face_eye(mianju_img)


