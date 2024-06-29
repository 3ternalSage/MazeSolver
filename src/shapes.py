from tkinter import Canvas


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

class Line:
    def __init__(self, point_a: Point, point_b: Point) -> None:
        self.p1: Point = point_a
        self.p2: Point = point_b
    
    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
