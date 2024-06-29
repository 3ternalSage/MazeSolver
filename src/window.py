from src.shapes import Line

from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.root: Tk = Tk()
        self.root.title = "Maze"
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.canvas: Canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        self.running_canvas: bool = False
    
    def redraw(self) -> None:
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self) -> None:
        self.running_canvas: bool = True
        while self.running_canvas:
            self.redraw()
        
    def close(self) -> None:
        self.running_canvas: bool = False
    
    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)