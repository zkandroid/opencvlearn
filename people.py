#coding:utf-8
import cv2
import numpy as np
from imutils.object_detection import non_max_suppression
import imutils

def people():
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    imge = cv2.imread("/home/zk/opencvtest/opencvlearn/people.jpg")
    grap = cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)
    (rects, weights) = hog.detectMultiScale(grap, winStride=(4, 4),
                    padding=(8, 8), scale=1.05)

        # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(imge, (x, y), (x + w, y + h), (0, 0, 255), 2)
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(imge, (xA, yA), (xB, yB), (0, 255, 0), 2)
    cv2.imshow("imge",imge)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()





if __name__== "__main__":
    people()
