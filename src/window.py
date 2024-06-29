from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.root = Tk()
        self.root.title = "Maze"
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root)
        self.canvas.pack()
        self.running_canvas = False
    
    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.running_canvas = True
        while self.running_canvas:
            self.redraw()
        
    def close(self):
        self.running_canvas = False