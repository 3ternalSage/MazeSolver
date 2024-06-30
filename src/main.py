import sys
sys.path.append('.')

from src.window import Window
from src.shapes import Line, Point, Cell
from src.maze import Maze

def main() -> None:
    win: Window = Window(800, 600)
    maze: Maze = Maze(10, 10, 40, 30, 10, 10, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r()
    maze._reset_cells_visited()
    
    maze._solve_r()
    win.wait_for_close()

if __name__ == '__main__':
    main()