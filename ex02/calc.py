import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, f"{txt}")

def equal_click(event):
    fun = entry.get()
    result = eval(fun)
    entry.delete(0,len(fun))
    entry.insert(tk.END, str(result))
    entry.grid(row=0, column=0, columnspan=3)

calc = tk.Tk()
calc.title("電卓")
calc.geometry("300x600")

entry = tk.Entry(calc, justify="right", width=10, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=3)

for i in range(10):
    button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30),text=f"{9-i}")
    button.bind("<1>", button_click)
    button.grid(row=i//3+1, column=i%3)

button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30), text="+")
button.bind("<1>", button_click)
button.grid(row=4, column=1)

button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30), text="=")
button.bind("<1>", equal_click)
button.grid(row=4, column=2)

calc.mainloop()