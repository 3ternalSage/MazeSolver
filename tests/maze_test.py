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
        win: Window | None = None #Window(width=800, height=600)
        m2: Maze = Maze(10, 10, num_rows, num_cols, 20, 20, win)
        m2._break_entrance_and_exit()
        # win.wait_for_close()
    
    def test_maze_gen_maze(self) -> None:
        num_cols: int = 18
        num_rows: int = 14
        win: Window = Window(width=800, height=600)
        m3: Maze = Maze(10, 10, num_rows, num_cols, 20, 20, win)
        m3._break_entrance_and_exit()
        m3._break_walls_r(debug=True)

        for x in m3._cells:
            for y in x:
                self.assertTrue(y.visited)
        m3._reset_cells_visited()

        for x in m3._cells:
            for y in x:
                self.assertFalse(y.visited)
        
        win.close()
    
    def test_maze_solve(self) -> None:
        num_cols: int = 18
        num_rows: int = 14
        win: Window = Window(width=800, height=600)
        m3: Maze = Maze(10, 10, num_rows, num_cols, 20, 20, win)
        m3._break_entrance_and_exit()
        m3._break_walls_r()
        m3._reset_cells_visited()

        print("Beginning solve...")
        print(m3._solve_r())


        win.wait_for_close()

if __name__ == '__main__':
    unittest.main()