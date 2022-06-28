import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    move = {"Up":[0, -1], "Down":[0, 1], "Right":[1, 0], "Left":[-1, 0], "":[0,0]}
    if maze[my+move[key][1]][mx+move[key][0]] == 0:
        mx += move[key][0]
        my += move[key][1]
    cx = mx * 100 + 50
    cy = my * 100 + 50
    canvas.coords("kokaton", cx, cy)
    root.after(50, main_proc)
    
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root,
                       width=1500,
                       height=900,
                       background="black"
                       )
    
    maze =  maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, maze)

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