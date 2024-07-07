import pyttsx3

if __name__ == "__main__":
    while True:
           x = input("Enter what you want to speak:\n")
           engine = pyttsx3.init()
           engine.say(x)
           engine.runAndWait()

 
"""
For MacOS:

import os

if __name__ == "__main__":
    while True: 
        x = input("Enter what you want to speak:\n")
        command = f"say {x}"
        os.system(command)
"""