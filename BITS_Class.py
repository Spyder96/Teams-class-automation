
import time 
from datetime import datetime 
import pyautogui
from pynput.keyboard import Controller
from pynput.keyboard import Key
import webbrowser as wb



dataWarehouse='https://teams.microsoft.com/l/meetup-join/19%3ameeting_MzlkZTIwYjctNjk3NC00YjgxLTlmOGEtZTA4OTM0MThjNTVh%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%2290c83da1-fa35-474f-ae47-5367415cc22e%22%7d'
operatingSystem='https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZTE1NjdjODctN2NlNy00YTM2LTllZWQtZmY4ZTcwODc4NjQ5%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%22bcc87f62-9dc8-4a1f-84be-4bcae2d8b485%22%7d'
computerNetworks='https://teams.microsoft.com/l/meetup-join/19%3ameeting_ODE5MDMxYjQtMzc0OC00ZGJjLWI5NmItYjYzMTFiYTJjOTMz%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%226400f058-59c6-4d48-9c30-a2600c8b2438%22%7d'
database='https://teams.microsoft.com/l/meetup-join/19%3ameeting_OGRjNzgyZjAtNDgxYS00ZDk0LWJlYzMtZjcyMDQyYzg3YjYx%40thread.v2/0?context=%7b%22Tid%22%3a%22e24ac094-efd8-4a6b-98d5-a129b32a8c9a%22%2c%22Oid%22%3a%226400f058-59c6-4d48-9c30-a2600c8b2438%22%7d'

lst=[
     [dataWarehouse, '08:55', '10:35'],
     [operatingSystem, '10:55', '12:35'],
     [computerNetworks, '13:55', '15:35'],
     [database, '15:55', '17:35']
     ]


#input lecture stats in form of list ......
# ["Link", start_time, end_time ]
# give time in 24 hrs format...
keyboard= Controller()
i=0
time_left=0

is_class_started =False

for lecture  in lst:
    while True:
    #Checking for end timing of the selected class and skipping if required
    #Program run after the end of selected class
        if ((datetime.now().hour*100) + datetime.now().minute) >= lecture[2]:
            i+=1
            break
        # while True :
        #     if is_class_started==False:
        #         if ((datetime.now().hour*100) + datetime.now().minute) >= lecture[2]:
        #             break;
        
        #Checking for end timing of the selected class and joining if time left
        #Program run during the selected class
        elif (datetime.now().hour*100 + datetime.now().minute >= lecture[1]) and (((datetime.now().hour*100) + datetime.now().minute) < lecture[2]):
            
             wb.open(lecture[0])
             is_class_started=True
             time.sleep(30)
             for i in range (7):
                 pyautogui.press('tab')
             time.sleep(1)
             pyautogui.press('enter')
             time.sleep(5)
             
        #Program run before the selected class timings     
        elif   (datetime.now().hour*100 + datetime.now().minute < lecture[1]):
            
            time_left=lecture[1]-(datetime.now().hour*100 + datetime.now().minute)
            time.sleep(time_left*10) 
            
        while is_class_started:
            time_left=lecture[2]-(datetime.now().hour*100 + datetime.now().minute)
            time.sleep(time_left*10)       #class joined, sleeping for the class period
            
            if time_left ==0:              #exiting
                is_class_started=False
                pyautogui.hotkey('ctrl','shift','h')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                break;

                
