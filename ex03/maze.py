import tkinter as tk

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

    root.mainloop()