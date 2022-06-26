
import time 
from datetime import datetime 
import pyautogui
from pynput.keyboard import Controller
from pynput.keyboard import Key
import webbrowser as wb



lst=[
     ['https://teams.microsoft.com/l/meetup-join/19%3ameeting_NmJhN2E2YzAtZWEwNy00OGIyLWI4YTYtNjdhODc4NTlhNWE5%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%2290c83da1-fa35-474f-ae47-5367415cc22e%22%7d', 855, 1035],
     ['https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZTE1NjdjODctN2NlNy00YTM2LTllZWQtZmY4ZTcwODc4NjQ5%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%22bcc87f62-9dc8-4a1f-84be-4bcae2d8b485%22%7d', 1055, 1235],
     ['https://teams.microsoft.com/l/meetup-join/19%3ameeting_NTk4MGQyNzYtN2M0Yi00ZTZjLWI0NzYtNTQwOWVlZGJmNDAw%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%226e87e067-c2c2-4036-8a2f-2c2f0973f5c7%22%7d', 1355, 1535],
     ['https://teams.microsoft.com/l/meetup-join/19%3ameeting_YjE2NzFjMmEtNmQ1Mi00MzBhLWJkODctZmExMjI2ZGM3Mjll%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%22de1d3b87-021b-4dbb-95df-93eab2f143bd%22%7d', 1555, 1735]
     
     ]


#input lecture stats in form of list ......
# ["Link", start_time, end_time ]
# give time in 24 hrs format...
keyboard= Controller()
i=0
time_left=0

is_class_started =False

for lecture  in lst:
    
    # Checking for end timing of the selected class and skipping if required
    #Program run after the end of selected class
    if ((datetime.now().hour*100) + datetime.now().minute) >= lecture[2]:
        i+=1;
        continue
    # while True :
    #     if is_class_started==False:
    #         if ((datetime.now().hour*100) + datetime.now().minute) >= lecture[2]:
    #             break;
    
    #Checking for end timing of the selected class and joining if time left
    #Program run during the selected class
    elif (datetime.now().hour*100 + datetime.now().minute >= lecture[1]) and (((datetime.now().hour*100) + datetime.now().minute) < lecture[2]):
        
         wb.open(lecture[0])
         is_class_started=True
         time.sleep(20)
         for i in range (7):
             pyautogui.press('tab')
         time.sleep(1)
         pyautogui.press('enter')
         time.sleep(5)
         time_left=lecture[2]-lecture[1]
        # pyautogui.hotkey('ctrl','shift','m')
        
         time.sleep(time_left*10)       #class joined, sleeping for the class period
         
         #exiting
         is_class_started=False
         pyautogui.hotkey('ctrl','shift','h')
         time.sleep(3)
         pyautogui.hotkey('alt','f4')
         time.sleep(3)
         pyautogui.hotkey('alt','f4')
         
         
    #Program run before the selected class timings     
    elif   (datetime.now().hour*100 + datetime.now().minute < lecture[1]):
        
        time_left=lecture[1]-(datetime.now().hour*100 + datetime.now().minute)
        time.sleep(time_left*10) 
                # is_class_started=False
                # pyautogui.hotkey('ctrl','shift','h')
                # time.sleep(3)
                # pyautogui.hotkey('alt','f4')
                # time.sleep(3)
                # pyautogui.hotkey('alt','f4')
                #time.sleep(3)
                #pyautogui.hotkey('alt','f4')
                #break   
    

                
