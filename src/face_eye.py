#coidng:utf_8
import numpy as np
import cv2
import face_recognition

#正脸
face_cascade = cv2.CascadeClassifier('/home/ly/opencv/data/haarcascades_cuda/haarcascade_frontalface_default.xml')
#侧脸
#face_cascade = cv2.CascadeClassifier('/home/ly/opencv/data/haarcascades/haarcascade_profileface.xml')
#
#face_cascade = cv2.CascadeClassifier('/home/ly/opencv/data/haarcascades_cuda/haarcascade_frontalface_alt_tree.xml')

#face_cascade = cv2.CascadeClassifier('/home/ly/opencvtest/haar/face_cascades/HS.xml')
eye_cascade = cv2.CascadeClassifier('/home/ly/opencv/data/haarcascades/haarcascade_eye.xml')
def face_eye():
	cap = cv2.VideoCapture(0)
	while(True):
		#获取视频及返回状态
		ret, img = cap.read()
		img1 = cv2.imread('/home/ly/opencvtest/haar/huge2.jpg')
		#将获取的视频转化为灰色
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		#检测视频中的人脸，并用vector保存人脸的坐标、大小（用矩形表示）
		#faces = face_recognition.face_locations(gray,1)
		#print(face_recognition.face_locations(gray,1))
		faces = face_cascade.detectMultiScale(gray, 1.1, 1)
		#脸部检测
		for (x,y,w,h) in faces:
			cv2.rectangle(img,(x+w,y+w),(w,h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
			#检测视频中脸部的眼睛，并用vector保存眼睛的坐标、大小（用矩形表示）
			eyes = eye_cascade.detectMultiScale(roi_gray,1.3,8)
			#眼睛检测
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		cv2.imshow('img',img)
		#按q键退出while循环
		if cv2.waitKey(30) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

def face():
	cap = cv2.VideoCapture(0)
	while(True):
		ret,img = cap.read()
		print(type(img))
		gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		face_cascade = cv2.CascadeClassifier('/home/ly/opencvtest/haar/face_cascades/haarcascade_frontalface_default.xml')
		faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.4,minNeighbors=1,minSize=(30,30),flags= 1)
		print('weight ---',weight)
		for (x,y,w,h) in faces :
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
			#检测视频中脸部的眼睛，并用vector保存眼睛的坐标、大小（用矩形表示）
			eyes = eye_cascade.detectMultiScale(roi_gray,1.3,9)
			#眼睛检测
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		cv2.imshow('imgface',img)
		if cv2.waitKey(30) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
			
def fullbody():
	#cap = cv2.VideoCapture("/home/ly/opencvtest/videostest/ks10013600.mp4")
	#fullbody_cascade = cv2.CascadeClassifier('/home/ly/opencv/data/haarcascades/haarcascade_fullbody.xml')
	fullbody_cascade = cv2.CascadeClassifier('/home/ly/opencv/data/haarcascades_cuda/haarcascade_fullbody.xml')
	while(True):
		#ret,img = cap.read()
		img = cv2.imread("/home/ly/opencvtest/neg/fullbody.jpg")
		gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		fullbody = fullbody_cascade.detectMultiScale(gray,scaleFactor = 1.05,minNeighbors=1)
		for (x,y,w,h) in fullbody:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imshow('imgbody',img)
		if cv2.waitKey(30) & 0xFF == ord('q'):
			break
	#cap.release()
	cv2.destroyAllWindows() 	
		
if __name__ == "__main__":
	#face_eye()
	face()
	#fullbody()
	
