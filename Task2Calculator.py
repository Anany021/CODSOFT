import tkinter as tk
from tkinter import *
def button_click(char):
 current_expression = entry.get()
 entry.delete(0, tk.END)
 entry.insert(tk.END, current_expression + char)
def calculate():
 try:
     result = eval(entry.get())
     entry.delete(0, tk.END)
     entry.insert(tk.END, result)
 except:
     entry.delete(0, tk.END)
     entry.insert(tk.END, "Invalid input!")
# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget
entry = tk.Entry(window, width=38,font=('Helvetica',25))
entry.grid(row=0, column=0, columnspan=200)
# Create the number buttons
btn_7 = tk.Button(window, text='7',height=2, width=15, command=lambda: button_click('7'),fg="Black",bg="White",font=('Helvetica',15))
btn_7.grid(row=1, column=0)
btn_8 = tk.Button(window, text='8',height=2, width=15, command=lambda: button_click('8'),fg="Black",bg="White",font=('Helvetica',15))
btn_8.grid(row=1, column=1)
btn_9 = tk.Button(window, text='9',height=2, width=15, command=lambda: button_click('9'),fg="Black",bg="White",font=('Helvetica',15))
btn_9.grid(row=1, column=2)
btn_divide = tk.Button(window, text='/', height=2,width=15, command=lambda: button_click('/'),fg="Black",bg="White",font=('Helvetica',15))
btn_divide.grid(row=1, column=3)
btn_4 = tk.Button(window, text='4',height=2, width=15, command=lambda: button_click('4'),fg="Black",bg="White",font=('Helvetica',15))
btn_4.grid(row=2, column=0)
btn_5 = tk.Button(window, text='5',height=2, width=15, command=lambda: button_click('5'),fg="Black",bg="White",font=('Helvetica',15))
btn_5.grid(row=2, column=1)
btn_6 = tk.Button(window, text='6', height=2,width=15, command=lambda: button_click('6'),fg="Black",bg="White",font=('Helvetica',15))
btn_6.grid(row=2, column=2)
btn_multiply = tk.Button(window, text='*', height=2,width=15, command=lambda: button_click('*'),fg="Black",bg="White",font=('Helvetica',15))
btn_multiply.grid(row=2, column=3)
btn_1 = tk.Button(window, text='1',height=2, width=15, command=lambda: button_click('1'),fg="Black",bg="White",font=('Helvetica',15))
btn_1.grid(row=3, column=0)
btn_2 = tk.Button(window, text='2',height=2, width=15, command=lambda: button_click('2'),fg="Black",bg="White",font=('Helvetica',15))
btn_2.grid(row=3, column=1)
btn_3 = tk.Button(window, text='3',height=2, width=15, command=lambda: button_click('3'),fg="Black",bg="White",font=('Helvetica',15))
btn_3.grid(row=3, column=2)
btn_subtract = tk.Button(window, text='-',height=2, width=15, command=lambda: button_click('-'),fg="Black",bg="White",font=('Helvetica',15))
btn_subtract.grid(row=3, column=3)
btn_0 = tk.Button(window, text='0', height=2,width=15, command=lambda: button_click('0'),fg="Black",bg="White",font=('Helvetica',15))
btn_0.grid(row=4, column=0)
btn_dot = tk.Button(window, text='.',height=2, width=15, command=lambda: button_click('.'),fg="Black",bg="White",font=('Helvetica',15))
btn_dot.grid(row=4, column=1)
btn_equals = tk.Button(window, text='=',height=2, width=15, command=calculate,fg="Black",bg="White",font=('Helvetica',15))
btn_equals.grid(row=4, column=2)
btn_add = tk.Button(window, text='+',height=2, width=15, command=lambda: button_click('+'),fg="Black",bg="White",font=('Helvetica',15))
btn_add.grid(row=4, column=3)
# Start the main event loop
window.configure(bg="Black")
window.mainloop()
