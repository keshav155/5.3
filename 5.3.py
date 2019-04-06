from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led = LED(4)


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
  
            
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            
            cipher += ' '
  
    return cipher 
  
 
def blink(message): 
    
    for letter in message: 
        if letter == '-':
            led.on()
            time.sleep(2)
            led.off()
            time.sleep(0.5)
        elif letter == '.':
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(0.5)
            # 1 space indicates different characters 
            # and 2 indicates different words 
             
    



win = Tk()
win.title("Morse code blinker")
win.geometry("640x640+100+100")

heading = Label(win,text = "Morse Code Blinker", font=("arial",20,"bold"), fg="steelblue").pack()

label1= Label(win,text= "Enter your name: ", font=("arial",20,"bold"),fg="black").place(x=10, y=200)

name = StringVar()
entry_box = Entry(win,textvariable = name, width=30,bg = 'cyan').place(x = 250, y = 210)
def final():
    name2 = str(name.get())
    final_name = name2.upper()
    result = encrypt(final_name)
    blink(result)

work = Button(win, text="Enter",width=30,height=5,bg = "lightblue", command = final).place(x = 250, y = 300)
def close():
    GPIO.cleanup()
    win.destroy()

win.mainloop()
win.protocol("WM_DELETE_WINDOW",close)

##morse code translator code and dictionary taken from : - https://www.geeksforgeeks.org/morse-code-translator-python/


