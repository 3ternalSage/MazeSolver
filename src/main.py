from src.window import Window
from src.shapes import Line, Point, Cell
from src.maze import Maze

def main() -> None:
    win: Window = Window(800, 600)

    maze: Maze = Maze(20, 20, 16, 12, 40, 40, win)
    
    win.wait_for_close()

if __name__ == '__main__':
    main()