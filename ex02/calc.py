import tkinter as tk
import tkinter.messagebox as tkm

num = False

# 数字ボタンの動作
def num_click(event):
    global num
    num = True
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, f"{txt}")

# =ボタン専用の動作
def equal_click(event):
    fun = entry.get()
    fun = fun.replace("×", "*")
    fun = fun.replace("÷", "/")
    result = eval(fun)
    entry.delete(0,tk.END)
    entry.insert(tk.END, str(result))
    entry.grid(row=0, column=0, columnspan=4)

# 四則演算とピリオドの動作
def button_click(event):
    global num
    if num:
        num = False
        btn = event.widget
        txt = btn["text"]
        entry.insert(tk.END, f"{txt}")

# ウィンドウ作成
calc = tk.Tk()
calc.title("電卓")
calc.geometry("400x600")

# 入力欄作成
entry = tk.Entry(calc, justify="right", width=13, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=4)

# 0~9のボタン作成
for i in range(9):
    button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30),text=f"{9-i}")
    button.bind("<1>", num_click)
    button.grid(row=i//3+1, column=2-i%3)
button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30),text="0")
button.bind("<1>", num_click)
button.grid(row=4, column=1)

# ピリオドボタン作成
piriod_button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30),text=".")
piriod_button.bind("<1>", button_click)
piriod_button.grid(row=4, column=0)

# 四則演算ボタン作成
mark = list("÷×-+")
for i,l in enumerate(mark,1):
    button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30), text=l)
    button.bind("<1>", button_click)
    button.grid(row=i, column=3)

# =ボタン作成
equal_button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30), text="=")
equal_button.bind("<1>", equal_click)
equal_button.grid(row=4, column=2)

calc.mainloop()