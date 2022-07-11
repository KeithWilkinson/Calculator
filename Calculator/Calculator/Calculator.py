from tkinter import *
import pygame

print("Calculator program started")

#Setup program window
root = Tk()
root.configure(bg ="#ADD8E6")
root.title("Calculator")

#Setup audio
pygame.mixer.init()
ClickSound = pygame.mixer.Sound("ButtonPress.wav")

#Setup input field
inputField = Entry(root, width=35, borderwidth=5)
inputField.grid(row=0, column=0, columnspan=3,padx=10,pady=10)

#Displays pressed button's value 
def buttonClick(number):
    current = inputField.get()
    inputField.delete(0,END)
    inputField.insert(0,str(current) + str(number))
    PlayClickSound()
    
#Clears input field
def buttonClear():
    inputField.delete(0,END)
    PlayClickSound()

#Perform addition operation
def buttonAdd():
    firstNumber=inputField.get()
    global fNum, operation
    operation = "addition"
    fNum = int(firstNumber)
    inputField.delete(0,END)
    PlayClickSound()

#Perform subtraction operation 
def buttonSubtract():
     firstNumber=inputField.get()
     global fNum, operation
     operation = "subtraction"
     fNum = int(firstNumber)
     inputField.delete(0,END)
     PlayClickSound()
    
#Perform multiplication operation
def buttonMultiply():
     firstNumber=inputField.get()
     global fNum, operation
     operation = "multiplication"
     fNum = int(firstNumber)
     inputField.delete(0,END)
     PlayClickSound()
    
#Perform division operation
def buttonDivide():
     firstNumber=inputField.get()
     global fNum, operation
     operation = "division"
     fNum = int(firstNumber)
     inputField.delete(0,END)
     PlayClickSound()

#Displays result of performed mathematical operation
def buttonEqual():
    secondNumber = inputField.get()
    PlayClickSound()
    inputField.delete(0,END)
    if operation == "addition":
       inputField.insert(0, fNum + int(secondNumber))
    if operation == "subtraction":
       inputField.insert(0, fNum - int(secondNumber))
    if operation == "multiplication":
       inputField.insert(0, fNum * int(secondNumber))
    if operation == "division":
       inputField.insert(0, fNum / int(secondNumber))

#Play click sound
def PlayClickSound():
    pygame.mixer.Sound.play(ClickSound)
   
#Define number buttons
button_1 = Button(root, text="1",padx=40,pady=20,bg ="#ADD8E6", command=lambda:buttonClick(1))
button_2 = Button(root, text="2",padx=40,pady=20,bg ="#ADD8E6", command=lambda:buttonClick(2))
button_3 = Button(root, text="3",padx=40,pady=20,bg ="#ADD8E6", command=lambda:buttonClick(3))
button_4 = Button(root, text="4",padx=40,pady=20,bg ="#ADD8E6", command=lambda:buttonClick(4))
button_5 = Button(root, text="5",padx=40,pady=20,bg ="#ADD8E6", command=lambda:buttonClick(5))
button_6 = Button(root, text="6",padx=40,pady=20,bg ="#ADD8E6", command=lambda:buttonClick(6))
button_7 = Button(root, text="7",padx=40,pady=20,bg ="#ADD8E6", command=lambda:buttonClick(7))
button_8 = Button(root, text="8",padx=40,pady=20,bg ="#ADD8E6", command=lambda:buttonClick(8))
button_9 = Button(root, text="9",padx=40,pady=20,bg ="#ADD8E6", command=lambda:buttonClick(9))
button_0 = Button(root, text="0",padx=40,pady=20,bg ="#ADD8E6", command=lambda:buttonClick(0))

#Define opewration buttons
button_Add = Button(root, text="+",padx=39,pady=20,bg ="#ADD8E6", command=buttonAdd)
button_Subtract = Button(root, text="-",padx=41,pady=20, bg ="#ADD8E6", command=buttonSubtract)
button_Multiply = Button(root, text="*",padx=40,pady=20,bg ="#ADD8E6", command=buttonMultiply)
button_Divide = Button(root, text="%",padx=41,pady=20,bg ="#ADD8E6", command=buttonDivide)
button_Equal = Button(root, text="=",padx=91,pady=20,bg ="#ADD8E6", command=buttonEqual)
button_Clear = Button(root, text="Clear",padx=79,pady=20,bg ="#ADD8E6", command=buttonClear)

#Display buttons
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_Clear.grid(row=4,column=1,columnspan=2)
button_Add.grid(row=5,column=0)
button_Equal.grid(row=5,column=1, columnspan=2)

button_Subtract.grid(row=6,column=0)
button_Multiply.grid(row=6,column=1)
button_Divide.grid(row=6,column=2)

#Main program loop
root.mainloop()