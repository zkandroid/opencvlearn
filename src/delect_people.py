#coding:utf-8
import cv2
import  numpy as np

def lvmu():
	cap = cv2.VideoCapture(0)
	while(True):
		#img=cv2.imread('/home/zk/opencvtest/opencvlearn/image/dog.jpg')
		ret,img = cap.read()
		#img=cv2.imread('/home/zk/opencvtest/opencvlearn/image/owen.jpeg')
		img_back=cv2.imread('/home/ly/opencvtest/opencvlearn/image/back.jpg')
		#print(img)
		#日常缩放
		rows,cols,channels = img_back.shape
		img_back=cv2.resize(img_back,None,fx=1,fy=2)
		#cv2.imshow('img_back',img_back)

		rows,cols,channels = img.shape
		img=cv2.resize(img,None,fx=0.8,fy=0.8)
		#cv2.imshow('img',img)
		rows,cols,channels = img.shape#rows，cols最后一定要是前景图片的，后面遍历图片需要用到

		#转换hsv
		hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		#获取mask
		#lower_blue=np.array([78,43,46])
		lower_blue=np.array([40,43,46])
		upper_blue=np.array([110,255,255])
		mask = cv2.inRange(hsv, lower_blue, upper_blue)
		cv2.imshow('Mask', mask)

		#腐蚀膨胀
		erode=cv2.erode(mask,None,iterations=1)
		#cv2.imshow('erode',erode)
		dilate=cv2.dilate(erode,None,iterations=1)
		#cv2.imshow('dilate',dilate)

		#遍历替换
		center=[50,50]#在新背景图片中的位置
		for i in range(rows):
    			for j in range(cols):
        			if dilate[i,j]==0:#0代表黑色的点
            				img_back[center[0]+i,center[1]+j]=img[i,j]#此处替换颜色，为BGR通道
		cv2.imshow('res',img_back)
		if cv2.waitKey(30) & 0xFF ==ord("q"):
			break
	cap.release()
	cv2.destroyAllWindows()

def bluetest():
    #img=cv2.imread('/home/zk/opencvtest/opencvlearn/image/dog.jpg')
    img=cv2.imread('/home/ly/opencvtest/opencvlearn/image/owen.jpeg')
    img_back=cv2.imread('/home/ly/opencvtest/opencvlearn/image/back.jpg')
    #print(img)
    #日常缩放
    rows,cols,channels = img_back.shape
    img_back=cv2.resize(img_back,None,fx=1,fy=2)
    #cv2.imshow('img_back',img_back)

    rows,cols,channels = img.shape
    img=cv2.resize(img,None,fx=0.3,fy=0.3)
    #cv2.imshow('img',img)
    rows,cols,channels = img.shape#rows，cols最后一定要是前景图片的，后面遍历图片需要用到

    #转换hsv
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #获取mask
    lower_blue=np.array([78,43,46])
    #lower_blue=np.array([40,43,46])
    upper_blue=np.array([110,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
#在lower_blue——upper之间的像素为0，否则为255，（蓝色区域就变成255（白色））
    cv2.imshow('Mask', mask)
    print('mask[0,0]',mask[10,10])

    #腐蚀膨胀
    erode=cv2.erode(mask,None,iterations=1)
    cv2.imshow('erode',erode)
    dilate=cv2.dilate(erode,None,iterations=1)
    cv2.imshow('dilate',dilate)

    #遍历替换
    center=[50,50]#在新背景图片中的位置
    for i in range(rows):
    	for j in range(cols):
            if mask[i,j]==0:#0代表黑色的点
            	img_back[center[0]+i,center[1]+j]=img[i,j]#此处替换颜色，为BGR通道
    cv2.imshow('res',img_back)
    if cv2.waitKey(0) & 0xFF ==ord("q"):
        cv2.destroyAllWindows()

if __name__ == "__main__":
	#lvmu()
        bluetest()
