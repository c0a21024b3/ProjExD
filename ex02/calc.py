import tkinter as tk
import tkinter.messagebox as tkm

# クリック時の動作
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, f"{txt}")

# =ボタン専用の動作
def equal_click(event):
    fun = entry.get()
    result = eval(fun)
    entry.delete(0,len(fun))
    entry.insert(tk.END, str(result))
    entry.grid(row=0, column=0, columnspan=3)

# ウィンドウ作成
calc = tk.Tk()
calc.title("電卓")
calc.geometry("300x600")

# 入力欄作成
entry = tk.Entry(calc, justify="right", width=10, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=3)

# 0~9のボタン作成
for i in range(10):
    button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30),text=f"{9-i}")
    button.bind("<1>", button_click)
    button.grid(row=i//3+1, column=i%3)

# ＋ボタン作成
plus_button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30), text="+")
plus_button.bind("<1>", button_click)
plus_button.grid(row=4, column=1)

# =ボタン作成
equal_button = tk.Button(calc, width=4, height=2, font=("Times New Roman", 30), text="=")
equal_button.bind("<1>", equal_click)
equal_button.grid(row=4, column=2)

calc.mainloop()