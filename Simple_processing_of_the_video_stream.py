import numpy as np
import cv2
import time
import math
from statistics import mode
cap = cv2.VideoCapture('C:/Users/Лев/Downloads/42.mp4')
ret_c, pre_frame=cap.read()
cur_frame=pre_frame.copy()
H, W = pre_frame.shape[:2]
faces=0
start_time = time.time()
shag=5
while ret_c==True:
    pre_gray = cv2.cvtColor(pre_frame, cv2.COLOR_BGR2GRAY)
    cur_gray = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)
    frame_diff = cv2.absdiff(cur_gray, pre_gray)
    dif=False
    for i in range(H-1,-1,-1):
        for j in range(W-(H%shag),-1,-1*shag):
            if frame_diff[i][j]>47:

'''Я просмотрел разницу пикселя [i][j] разных фото, таким способом я отсекаю немного измененную фотографию'''
                dif=True
                faces+=1
                break
        if dif==True:
            break
    #cv2.imshow('frame diff ', frame_diff)
    #cv2.imshow('pre', pre_gray)
    #cv2.imshow('cur',cur_gray)
    pre_frame = cur_frame.copy()
    ret_c, cur_frame = cap.read()
    #if cv2.waitKey(50) & 0xFF == ord('q'):
    #    break#2 строки, чтобы все ок работало
print(faces)
print(time.time()-start_time)cap.release()  # хз, что это
cv2.destroyAllWindows()
