import tkinter as tk

canvas = None

class Point:
    def draw(self):
        pass

    def onClick(self, event):
        pass

    def onMouseMove(self, event):
        pass

class NoPoints(Point):
    def onClick(self, event):
        global state
        state = OnePoint(event.x, event.y)

class OnePoint(Point):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def onMouseMove(self, event):
        canvas.create_line(self.x, self.y, event.x, event.y)

    def onClick(self, event):
        global state
        state = TwoPoints(self, event.x, event.y)

class TwoPoints(Point):
    def __init__(self, onePoint, x, y):
        self.onePoint = onePoint
        self.x = x
        self.y = y

    def onMouseMove(self, event):
        canvas.create_line(self.onePoint.x, self.onePoint.y, self.x, self.y)

    def onClick(self, event):
        global state
        state = OnePoint(event.x, event.y)

state = NoPoints()

class PythonRule():
    def __init__(self, root):
        self.root = root

        self.root.attributes('-fullscreen',True)
        self.root.attributes("-alpha", 0.3)

        global canvas
        canvas = tk.Canvas(self.root)
        canvas.pack(fill=tk.BOTH, expand=1)
        canvas.bind("<Button-1>", self.onClick)
        canvas.bind("<Motion>", self.onMouseMove)
        self.root.bind("<Escape>", self.onEscape)

    def onEscape(self, event):
        canvas.delete("all")
        global state
        state = NoPoints()

    def onMouseMove(self, event):
        canvas.delete("all")
        state.onMouseMove(event)

    def onClick(self, event):
        canvas.delete("all")
        state.onClick(event)

root = tk.Tk()
app = PythonRule(root)
root.mainloop()
