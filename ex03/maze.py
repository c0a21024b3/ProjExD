import tkinter as tk
import maze_maker
import tkinter.messagebox as tkm

yoko = 15 # 横のマス数
tate = 9  # 縦のマス数

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my, key
    move = {"Up":[0, -1], "Down":[0, 1], "Right":[1, 0], "Left":[-1, 0],"":[0, 0]}
    try:
        if maze[my+move[key][1]][mx+move[key][0]] != 1:
            mx += move[key][0]
            my += move[key][1]
    except:
        tkm.showerror("","矢印キーで動かしてください")
        key = ""
    
    cx = mx * 100 + 50
    cy = my * 100 + 50
    canvas.coords("kokaton", cx, cy)
    root.after(50, main_proc)
    # ゴール時の処理
    if maze[my][mx] == 2:
        maze[my][mx] = 0
        tkm.showinfo("Congratulations", "ゴールしました！")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root,
                       width=1500,
                       height=900,
                       background="black"
                       )
    
    maze =  maze_maker.make_maze(yoko, tate)
    maze_maker.show_maze(canvas, maze)

    # スタートマス作成
    canvas.create_rectangle(100, 100, 100+100, 100+100, 
                                    fill="yellow")
    # ゴールマス作成
    if maze[tate-2][yoko-3] == 1:
        maze[tate-2][yoko-2] = 2
        canvas.create_rectangle(100*(yoko-2), 100*(tate-2), 100*(yoko-2)+100, 100*(tate-2)+100, 
                                    fill="red")
    else:
        for y in range(tate-2, 0, -1):
            if maze[y-1][yoko-2] == 1:
                maze[y][yoko-2] = 2
                canvas.create_rectangle(100*(yoko-2), 100*(y), 100*(yoko-2)+100, 100*(y)+100, 
                                        fill="red")
                break
    
    kokaton = tk.PhotoImage(file="ex03/fig/0.png")
    cx, cy = 350, 450
    canvas.create_image(cx, cy, image=kokaton, tag="kokaton")
    canvas.pack()

    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    mx, my = 1, 1
    main_proc()

    root.mainloop()