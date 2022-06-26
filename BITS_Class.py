
import time 
from datetime import datetime 
import pyautogui
from pynput.keyboard import Controller
from pynput.keyboard import Key
import webbrowser as wb


    


lst=[
     ['https://teams.microsoft.com/l/meetup-join/19%3ameeting_NmJhN2E2YzAtZWEwNy00OGIyLWI4YTYtNjdhODc4NTlhNWE5%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%2290c83da1-fa35-474f-ae47-5367415cc22e%22%7d', '08:55', '10:35'],
     ['https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZTE1NjdjODctN2NlNy00YTM2LTllZWQtZmY4ZTcwODc4NjQ5%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%22bcc87f62-9dc8-4a1f-84be-4bcae2d8b485%22%7d', '10:55', '12:35'],
     ['https://teams.microsoft.com/l/meetup-join/19%3ameeting_NTk4MGQyNzYtN2M0Yi00ZTZjLWI0NzYtNTQwOWVlZGJmNDAw%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%226e87e067-c2c2-4036-8a2f-2c2f0973f5c7%22%7d', '13:55', '15:35'],
     ['https://teams.microsoft.com/l/meetup-join/19%3ameeting_YjE2NzFjMmEtNmQ1Mi00MzBhLWJkODctZmExMjI2ZGM3Mjll%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%22de1d3b87-021b-4dbb-95df-93eab2f143bd%22%7d', '15:55', '17:35']
     
     
     ]

#['https://teams.microsoft.com/l/meetup-join/19%3ameeting_YjEwOWNmZDMtMmQ5MC00NDM5LWFhZWUtMTY5NjZmZjJhMGI2%40thread.v2/0?context=%7b%22Tid%22%3a%226d28e4fb-9074-4a0b-a5b8-9a89f632cc60%22%2c%22Oid%22%3a%22377bd695-6601-4d9d-9bb1-bbd5cafd3784%22%7d','01:21','01:22']
#input lecture stats in form of list ......
# ["Link","start_time","end_time"]
# give time in 24 hrs format...
keyboard= Controller()

is_class_started =False
for lecture  in lst:
    while True :
        if is_class_started==False:
            if (datetime.now().hour >= int(lecture[2].split(':')[0])and 
                datetime.now().minute > int(lecture[2].split(':')[1])):
                break;
            else:
                wb.open(lecture[0])
                is_class_started=True
                time.sleep(20)
                for i in range (7):
                    pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(5)
               # pyautogui.hotkey('ctrl','shift','m')
                time.sleep(10)
        elif   (datetime.now().hour == int(lecture[2].split(':')[0]) and
                datetime.now().minute == int(lecture[2].split(':')[1])):
                is_class_started=False
                pyautogui.hotkey('ctrl','shift','h')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                #time.sleep(3)
                #pyautogui.hotkey('alt','f4')
                break

                
