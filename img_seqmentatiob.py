#coding:utf-8
import cv2 


def thresh_binary():
    image = cv2.imread("/home/zk/opencvtest/opencvlearn/image/dog.jpg")
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    t,thresh1 = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)
    t,thresh2 = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV)
    t,thresh3 = cv2.threshold(gray,128,255,cv2.THRESH_TRUNC)
    t,thresh4 = cv2.threshold(gray,128,255,cv2.THRESH_TOZERO)
    t,thresh5 = cv2.threshold(gray,128,255,cv2.THRESH_TOZERO_INV)
    cv2.imshow('Thresh_binary',thresh1)
    cv2.imshow('Thresh_binary_inv',thresh2)
    cv2.imshow('Thresh_trunc',thresh3)
    cv2.imshow('Thresh_tozero',thresh4)
    #cv2.imshow('Thresh_tozero_inv',thresh5)
    cv2.imshow('img',image)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindow()

def imgvector():
    img = cv2.imread("/home/zk/opencvtest/opencvlearn/people.jpg")
    vector =  img.shape
    print(vector)
    #vet2 = img.resize(500,330,3)
    #print(img.shape)
    raw = img.flatten()
    x =raw.shape
    means = cv2.mean(img)
    print('means ',means)
    print('raw.shape ',raw.shape)
    print('raw',raw)
    cv2.imshow("img",img)
    #cv2.imshow("means",means)
    #cv2.imshow("vet2",vet2)
    if cv2.waitKey(0) == 27:
        cv2.destoryAllWindows()


if __name__=="__main__":
    #thresh_binary()
    imgvector()

