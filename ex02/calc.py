import tkinter as tk
import tkinter.messagebox as tkm
import random 

check_num = False # 直前の文字が数字かの判断
width = 4 # ボタンの横幅
height = 1 # ボタンの縦幅

# 数字と％の動作
def num_click(event):
    global check_num
    check_num = True
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, f"{txt}")

# =ボタン専用の動作
def equal_click(event):
    fun = entry.get()
    fun = fun.replace("×", "*")
    fun = fun.replace("÷", "/")
    fun = fun.replace("^", "**")
    fun = fun.replace("%", "/100")
    result = eval(fun)
    entry.delete(0,tk.END)
    entry.insert(tk.END, str(result))
    entry.grid(row=0, column=0, columnspan=4)

# 四則演算,ピリオドの動作
def button_click(event):
    global check_num
    if check_num:
        check_num = False
        btn = event.widget
        txt = btn["text"]
        entry.insert(tk.END, f"{txt}")

# 全消去ボタンの動作
def alldel_click(event):
    entry.delete(0, tk.END)
    entry.grid(row=0, column=0, columnspan=4)

# 消去ボタンの動作
def del_click(event):
    fun = entry.get()
    entry.delete(len(fun)-1,tk.END)
    entry.grid(row=0, column=0, columnspan=4)

# 隠しボタンの動作
def hide_click(event):
    num_list = list("0123456789")
    random.shuffle(num_list)
    for i in range(9):
        button = tk.Button(calc, width=width, height=height, font=("Times New Roman", 30),text=num_list.pop())
        button.bind("<1>", num_click)
        button.grid(row=i//3+2, column=2-i%3)
    button = tk.Button(calc, width=width, height=height, font=("Times New Roman", 30),text=num_list.pop())
    button.bind("<1>", num_click)
    button.grid(row=5, column=1)
    tkm.showinfo("隠し機能", "数字をシャッフルしました")

# ウィンドウ作成
calc = tk.Tk()
calc.title("電卓")
calc.geometry("392x500")

# 入力欄作成
entry = tk.Entry(calc, justify="right", width=13, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=4)

# 0~9のボタン作成
for i in range(9):
    button = tk.Button(calc, width=width, height=height, font=("Times New Roman", 30),text=f"{9-i}")
    button.bind("<1>", num_click)
    button.grid(row=i//3+2, column=2-i%3)
button = tk.Button(calc, width=width, height=height, font=("Times New Roman", 30),text="0")
button.bind("<1>", num_click)
button.grid(row=5, column=1)

# ピリオドボタン作成
piriod_button = tk.Button(calc, width=width, height=height, font=("Times New Roman", 30),text=".")
piriod_button.bind("<1>", button_click)
piriod_button.grid(row=5, column=0)

# 四則演算ボタン作成
mark = list("÷×-+")
for i,l in enumerate(mark,2):
    button = tk.Button(calc, width=width, height=height, font=("Times New Roman", 30), text=l)
    button.bind("<1>", button_click)
    button.grid(row=i, column=3)

# =ボタン作成
equal_button = tk.Button(calc, width=width, height=height, font=("Times New Roman", 30), text="=")
equal_button.bind("<1>", equal_click)
equal_button.grid(row=5, column=2)

# 全消去ボタン作成
alldel_button = tk.Button(calc, width=width, height=height, font=("Times New Roman", 30), text="C")
alldel_button.bind("<1>", alldel_click)
alldel_button.grid(row=1, column=0)

# 累乗ボタン作成
ex_button = tk.Button(calc, width=width, height=height, font=("Times New Roman", 30), text="^")
ex_button.bind("<1>", button_click)
ex_button.grid(row=1, column=1)

# %ボタン作成
par_button = tk.Button(calc, width=width, height=height, font=("Times New Roman", 30), text="%")
par_button.bind("<1>", num_click)
par_button.grid(row=1, column=2)

# 消去ボタン作成
del_button = tk.Button(calc, width=width, height=height, font=("Times New Roman", 30), text="◁")
del_button.bind("<1>", del_click)
del_button.grid(row=1, column=3)

# 隠しボタン追加
hide_button = tk.Button(calc, width=width, height=height*8, font=("Times New Roman", 30), text="?")
hide_button.bind("<1>", hide_click)
hide_button.grid(row=1, column=5, rowspan=5)

calc.mainloop()