import cognitive_face as CF
import os

KEY = ''  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = ''  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

position = input()


def turn_left(resultp, i):
    result2 = resultp[0]['faceAttributes']['headPose']['yaw']
    if (result2 > 15.0):
        return str(i)
    else:
        return ''


def turn_right(resultp, i):
    result2 = resultp[0]['faceAttributes']['headPose']['yaw']
    if (result2 < -15.0):
        return str(i)
    else:
        return ''


def roll_left(resultp, i):
    result2 = resultp[0]['faceAttributes']['headPose']['roll']
    if (result2 > 15.0):
        return str(i)
    else:
        return ''


def roll_right(resultp, i):
    result2 = resultp[0]['faceAttributes']['headPose']['roll']
    if (result2 < -15.0):
        return str(i)
    else:
        return ''


files = os.listdir('<Свой путь>')

otvet = ''
for i in range(0,len(files)):
    img_url = '<Свой путь>' + str(i)+'.jpg'
    result = CF.face.detect(img_url, face_id=False, landmarks=False, attributes="headPose")
    print(result)
    switch_case = {
        'turn left': turn_left(result, i),
        'turn right': turn_right(result, i),
        'roll left': roll_left(result, i),
        'roll right': roll_right(result, i)
    }
    if(switch_case[position] !=''):
        otvet=otvet+switch_case[position]+' '
    print(otvet)

print(otvet)
