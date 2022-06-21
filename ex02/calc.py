import tkinter as tk
import tkinter.messagebox as tkm

calc = tk.Tk()
calc.title("電卓")
calc.geometry("300x500")

for i in range(10):
    button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30),text=f"{9-i}")
    button.grid(row=i//3, column=i%3)

calc.mainloop()