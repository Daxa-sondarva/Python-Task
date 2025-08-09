#Assignment 6
#module 10 & 11 : CALCULATOR USING TKINTER
#step 1 : importing
from tkinter import *

#step 2 : Gui interaction
window = Tk()
window.geometry("500x500")
window.title("Calculator")

#step 3 : adding
#Entery box
entry = Entry(window, width=30, font=("Arial", 18),borderwidth=3,relief="ridge")
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

#Add a Function to Insert Numbers into Entry
def button_click(number):
    current = entry.get() # Get current Text in entry
    entry.delete(0, END)  #clear Entry
    entry.insert(0,current + str(number)) #Add clicked number

def button_clear():
    entry.delete(0, END)#clear Entry

def button_operation(op):
    current = entry.get() # Get current oprator in entry
    entry.delete(0,END)#clear Entry
    entry.insert(0,current + op )#Add clicked operator


def button_equal():
    try:
        result = str(eval(entry.get())) # eval executes the math string
        entry.delete(0, END)
        entry.insert(0,result)
    except:
        entry.delete(0,END)
        entry.insert(0,"Error")

def button_backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])


#number button
buttons = {}
for num in range(10):
    buttons[num] = Button(window, text=str(num),padx=40,pady=20,font=('Arial',14),command=lambda x=num:button_click(x))


#Create Number Buttons
button_1 = Button(window, text="1", padx=40, pady=20,font=('Arial',14), command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20,font=('Arial',14), command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20,font=('Arial',14), command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20,font=('Arial',14), command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20,font=('Arial',14), command=lambda: button_click(5))
button_6= Button(window, text="6", padx=40, pady=20,font=('Arial',14), command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20,font=('Arial',14), command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20,font=('Arial',14), command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20,font=('Arial',14), command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20,font=('Arial',14), command=lambda: button_click(0))

#operator Button
button_add = Button(window,text="+",padx=40,pady=20,font=('Arial',14),command=lambda: button_operation('+'))
button_sub = Button(window,text="-",padx=40,pady=20,font=('Arial',14),command=lambda: button_operation('-'))
button_mul = Button(window,text="*",padx=40,pady=20,font=('Arial',14),command=lambda: button_operation('*'))
button_div = Button(window,text="/",padx=40,pady=20,font=('Arial',14),command=lambda: button_operation('/'))

button_equal = Button(window, text="=", padx=40, pady=20, font=('Arial',14), command=button_equal)
button_clear = Button(window, text="C", padx=40, pady=20, font=('Arial',14), command=button_clear)

button_backspace = Button(window, text="<-", padx=40, pady=20, font=('Arial',14), command=button_backspace)


#Arrange buttons on the grid

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_sub.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

# button_0.grid(row=4, column=1) 
button_clear.grid(row=4, column=0)
buttons[0].grid(row=4, column=1) # Centered in bottom row
button_equal.grid(row=4, column=2)
button_div.grid(row=4, column=3)
button_backspace.grid(row=5, column=1)

#step 4 : mainloop
mainloop()
