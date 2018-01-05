#coding:utf-8
import cv2
import numpy as np


mianju_img = cv2.imread('/home/ly/opencvtest/opencvlearn/image/mianju.jpg')
mianju_img = cv2.resize(mianju_img,(32,32))
cv2.imshow('mianju',mianju_img)
if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()
