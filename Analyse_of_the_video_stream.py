import numpy as np
import cv2
import time
import math
from statistics import mode
def Is_New_Face(Faces, new_face,H,W):
    ident = True
    if Faces.__len__()==0:
        return True
    for pat in Faces:
        ident =True
        frame_diff=cv2.absdiff(pat, new_face)
        for i in range(H - 1, -1, -1):
            for j in range(W - (H % 5), -1, -5):
                if frame_diff[i][j] > 50:
                    ident=False
                    break
            if ident == False:
                break
        if ident==True:
            break
    if ident == False:
        return True
    else:
        return False
cap = cv2.VideoCapture('C:/Users/Лев/Downloads/133.mp4')
ret_c, pre_frame=cap.read()
cur_frame=pre_frame.copy()
H, W = pre_frame.shape[:2]faces=0
start_time = time.time()
shag=5faces_list=[]
while ret_c==True:
    pre_gray = cv2.cvtColor(pre_frame, cv2.COLOR_BGR2GRAY)
    cur_gray = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)
    frame_diff = cv2.absdiff(cur_gray, pre_gray)
    dif=False
    for i in range(H-1,-1,-1):
        for j in range(W-(H%shag),-1,-1*shag):
            if frame_diff[i][j]>50:
                dif=True
                break
        if dif==True:
            if Is_New_Face(faces_list, cur_gray, H, W):
                faces += 1
                faces_list.append(cur_gray)
            break
    #cv2.imshow('frame diff ', frame_diff)
    #cv2.imshow('pre', pre_gray)
    #cv2.imshow('cur',cur_gray)
    pre_frame = cur_frame.copy()
    ret_c, cur_frame = cap.read()    
#if cv2.waitKey(50) & 0xFF == ord('q'):
    #    break#2 строки, чтобы все ок работало
print(faces)
print(time.time()-start_time)
cap.release()  # хз, что это
cv2.destroyAllWindows()
