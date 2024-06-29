import sys
sys.path.append('.')
from src.window import Window
from src.shapes import Line, Point, Cell
from src.maze import Maze

import unittest


class Tests(unittest.TestCase):
    def test_maze_create_cells(self) -> None:
        num_cols: int = 12
        num_rows: int = 10
        m1: Maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        

        self.assertEqual(len(m1._cells), num_cols)

        self.assertEqual(len(m1._cells[0]), num_rows)

    
    def test_maze_break_entrance_exit(self) -> None:
        num_cols: int = 18
        num_rows: int = 14
        win: Window = Window(width=800, height=600)
        m2: Maze = Maze(10, 10, num_rows, num_cols, 20, 20, win)
        m2._break_entrance_and_exit()
        win.wait_for_close()

if __name__ == '__main__':
    unittest.main()