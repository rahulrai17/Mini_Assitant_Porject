from os import startfile, write
from tkinter import Message
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
import Main as main

def whatsapp():

    main.speak("i can message or call or video call or view status for you sir ,what would you like to choose")
    choice = main.TakeCommand()
    main.speak("Starting Whatsapp, sir")
    startfile("C:\\Users\\raira\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    
    if 'message' in choice:
        main.speak("Reciver's name ,sir")
        name = main.TakeCommand()
        main.speak("And what is your Message ,sir")
        message = main.TakeCommand()
        main.speak("okay sir")
        sleep(2)
        click(x=142, y=146)
        sleep(1)
        write(name)
        sleep(1)
        click(x=463, y=290)
        sleep(2)
        click(x=927, y=980)
        sleep(1)
        write(message)
        sleep(1)
        press('enter')

    elif "make call" in choice:
        main.speak("Reciver's name ,sir")
        name = main.TakeCommand()
        main.speak("okay sir")
        sleep(2)
        click(x=142, y=146)
        sleep(1)
        write(name)
        sleep(1)
        click(x=463, y=290)
        sleep(2)
        click(x=1717, y=71)

    elif "video call" in choice:
        main.speak("Reciver's name ,sir")
        name = main.TakeCommand()
        main.speak("okay sir")
        sleep(2)
        click(x=142, y=146)
        sleep(1)
        write(name)
        sleep(1)
        click(x=463, y=290)
        sleep(2)
        click(x=1671, y=73)

    elif "view status" in choice:
        main.speak("opening Status sir")
        sleep(10)
        click(x=414, y=75)
        sleep(1)
        click(x=463, y=290)        


   
