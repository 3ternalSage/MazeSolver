import typing
if typing.TYPE_CHECKING:
    from src.window import Window

from src.shapes import Cell

import time

class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window) -> None:
        self.x1: int = x1
        self.y1: int = y1
        self.num_rows: int = num_rows
        self.num_cols: int = num_cols
        self.cell_size_x: int = cell_size_x
        self.cell_size_y: int = cell_size_y
        self._win: Window = win
        self._cells: list[list[Cell]] = None
        self._create_cells()
        self._animate()
    
    def _create_cells(self) -> None:
        self._cells = [[self._draw_cell(i, j) for i in range(self.num_rows)] for j in range(self.num_cols)]
    
    def _draw_cell(self, i: int, j: int) -> Cell:
        c = Cell(
            self.x1 + (self.cell_size_x * i),
            self.y1 + (self.cell_size_y * j),
            self.x1 + (self.cell_size_x * (i+1)),
            self.y1 + (self.cell_size_y * (j+1)),
            self._win
        )
        c.draw()
        return c
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)