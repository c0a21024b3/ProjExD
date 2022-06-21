import tkinter as tk
import tkinter.messagebox as tkm

def num_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, f"{txt}")


calc = tk.Tk()
calc.title("電卓")
calc.geometry("300x600")

entry = tk.Entry(calc, justify="right", width=10, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=3)

for i in range(10):
    button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30),text=f"{9-i}")
    button.bind("<1>", num_click)
    button.grid(row=i//3+1, column=i%3)

calc.mainloop()