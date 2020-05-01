import tkinter as tk

class PythonRule():
    points = []

    def __init__(self, root):
        self.root = root

        self.root.attributes('-fullscreen',True)
        self.root.attributes("-alpha", 0.5)

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.canvas.bind("<Button-1>", self.onClick)

    def onClick(self, event):
        self.canvas.delete("all")
        if len(self.points) == 2:
            self.points.pop(0)
        self.points.append((event.x, event.y))
        if len(self.points) == 2:
            self.canvas.create_line(
                self.points[0][0],
                self.points[0][1],
                self.points[1][0],
                self.points[1][1],
            )

root = tk.Tk()
app = PythonRule(root)
root.mainloop()
