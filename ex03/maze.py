import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root,
                       width=1500,
                       height=900,
                       background="black"
                       )
    kokaton = tk.PhotoImage(file="ex03/fig/0.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=kokaton, tag="kokaton")
    canvas.pack()

    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.mainloop()