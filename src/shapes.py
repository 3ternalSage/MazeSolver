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

class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, window: 'Window') -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self._x1: int = x1
        self._y1: int = y1
        self._x2: int = x2
        self._y2: int = y2
        self._win: 'Window' = window

    def draw(self) -> None:
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), 'black')
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), 'black')
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), 'black')
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), 'black')
