import typing
if typing.TYPE_CHECKING:
    from src.window import Window

from src.shapes import Cell

import random
import time

class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: 'Window | None' = None, seed: int | None = None) -> None:
        self.x1: int = x1
        self.y1: int = y1
        self.num_rows: int = num_rows
        self.num_cols: int = num_cols
        self.cell_size_x: int = cell_size_x
        self.cell_size_y: int = cell_size_y
        self.seed = seed if seed else random.seed(seed)
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
            self._win if self._win else None
        )
        c.draw()
        return c
    
    def _animate(self) -> None:
        if self._win:
            self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self) -> None:
        if self._cells and self._cells[0]:
            self._cells[0][0].has_top_wall = False
            self._cells[0][0].draw()
            self._cells[-1][-1].has_bottom_wall = False
            self._cells[-1][-1].draw()

    def _break_walls_r(self, i: int = 0, j: int = 0, debug: bool = False) -> None:
        self._cells[i][j].visited = True
        while True:
            cells_to_visit: list[(int, int)] = []
            if (i-1) >= 0:
                cells_to_visit.append((i-1, j)) if not self._cells[i-1][j].visited else ()
            if (i+1) <= self.num_cols-1:
                cells_to_visit.append((i+1, j)) if not self._cells[i+1][j].visited else ()
            if (j-1) >= 0:
                cells_to_visit.append((i, j-1)) if not self._cells[i][j-1].visited else ()
            if (j+1) <= self.num_rows-1:
                cells_to_visit.append((i, j+1)) if not self._cells[i][j+1].visited else ()
            if not cells_to_visit:
                self._cells[i][j].draw()
                break
            else:
                x: int
                y: int
                random.shuffle(cells_to_visit)
                x, y = cells_to_visit.pop()
                if i+1 == x:
                    self._cells[x][y].has_top_wall = False
                    self._cells[i][j].has_bottom_wall = False
                elif i-1 == x:
                    self._cells[x][y].has_bottom_wall = False
                    self._cells[i][j].has_top_wall = False
                elif j+1 == y:
                    self._cells[x][y].has_left_wall = False
                    self._cells[i][j].has_right_wall = False
                elif j-1 == y:
                    self._cells[x][y].has_right_wall = False
                    self._cells[i][j].has_left_wall = False
                
                if debug:
                    self._cells[i][j].draw()
                    self._cells[x][y].draw()
                    self._cells[i][j].draw_move(self._cells[x][y])
                    self._animate()
                
                self._break_walls_r(x, y)
    
    def _reset_cells_visited(self) -> None:
        for x in self._cells:
            for y in x:
                y.visited = False
    
    def _solve_r(self, i: int = 0, j: int = 0, cost: int = 0) -> bool:
        self._animate()
        self._cells[i][j].visited = True
        x: int = self.num_cols-1
        y: int = self.num_rows-1
        if i == x and j == y:
            return True
        # print(f"getting cell 0 | {(i-1) >= 0} {not self._cells[i-1][j].visited} | {not self._cells[i][j].has_top_wall} | {not self._cells[i-1][j].has_bottom_wall}")
        cells_to_visit: list[tuple[int, tuple[int, int]]] = []
        if (i-1) >= 0:
            (cells_to_visit.append((cost+1+abs(i-1-x)+abs(j-y), (i-1, j))) if not self._cells[i-1][j].visited
                                                                          and not self._cells[i][j].has_top_wall 
                                                                          and not self._cells[i-1][j].has_bottom_wall else ())
        # print(f"getting cell 1 | {(i+1) <= self.num_cols-1} | {not self._cells[i+1][j].visited} | {not self._cells[i][j].has_bottom_wall} | {not self._cells[i+1][j].has_top_wall}")
        if (i+1) <= self.num_cols-1:
            (cells_to_visit.append((cost+1+abs(i+1-x)+abs(j-y), (i+1, j))) if not self._cells[i+1][j].visited 
                                                                          and not self._cells[i][j].has_bottom_wall 
                                                                          and not self._cells[i+1][j].has_top_wall else ())
        # print(f"getting cell 2 | {(j-1) >= 0} {not self._cells[i][j-1].visited} | {not self._cells[i][j].has_left_wall} | {not self._cells[i][j-1].has_right_wall}")
        if (j-1) >= 0:
            (cells_to_visit.append((cost+1+abs(i-x)+abs(j-1-y), (i, j-1))) if not self._cells[i][j-1].visited 
                                                                          and not self._cells[i][j].has_left_wall 
                                                                          and not self._cells[i][j-1].has_right_wall else ())
        # print(f"getting cell 3 | {(j+1) <= self.num_rows-1} | {not self._cells[i][j+1].visited} | {not self._cells[i][j].has_right_wall} | {not self._cells[i][j+1].has_left_wall}")
        if (j+1) <= self.num_rows-1:
            (cells_to_visit.append((cost+1+abs(i-x)+abs(j+1-y), (i, j+1))) if not self._cells[i][j+1].visited 
                                                                          and not self._cells[i][j].has_right_wall 
                                                                          and not self._cells[i][j+1].has_left_wall else ())
        cells_to_visit = sorted(cells_to_visit, reverse=True)
        # print(cells_to_visit, flush=True)

        while cells_to_visit:
            _, next_coords = cells_to_visit.pop()
            n_i, n_j = next_coords
            self._cells[i][j].draw_move(self._cells[n_i][n_j])
            solved: bool = self._solve_r(n_i, n_j, cost=cost+1)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[n_i][n_j], undo=True)

        return False
