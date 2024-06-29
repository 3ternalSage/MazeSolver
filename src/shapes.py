import typing
if typing.TYPE_CHECKING:
    from tkinter import Canvas
    from src.window import Window


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

class Line:
    def __init__(self, point_a: Point, point_b: Point) -> None:
        self.p1: Point = point_a
        self.p2: Point = point_b
    
    def draw(self, canvas: 'Canvas', fill_color: str) -> None:
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, window: 'Window | None' = None) -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self._x1: int = x1
        self._y1: int = y1
        self._x2: int = x2
        self._y2: int = y2
        self._win: Window = window

    def draw(self) -> None:
        if self._win:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), 'black' if self.has_left_wall else 'white')
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), 'black' if self.has_right_wall else 'white')
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), 'black' if self.has_top_wall else 'white')
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), 'black' if self.has_bottom_wall else 'white')

    def draw_move(self, to_cell: 'Cell', undo: bool = False):
        if self._win:
            self_center: Point = Point((self._x1+self._x2)/2, (self._y1+self._y2)/2)
            other_center: Point = Point((to_cell._x1+to_cell._x2)/2, (to_cell._y1+to_cell._y2)/2)
            self._win.draw_line(Line(self_center, other_center, 'gray' if undo else 'red'))