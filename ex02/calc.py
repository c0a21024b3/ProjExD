import tkinter as tk
import tkinter.messagebox as tkm

def num_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo("お知らせ", f"これは{txt}です。")

calc = tk.Tk()
calc.title("電卓")
calc.geometry("300x500")

for i in range(10):
    button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30),text=f"{9-i}")
    button.bind("<1>", num_click)
    button.grid(row=i//3, column=i%3)

calc.mainloop()