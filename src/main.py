import sys
sys.path.append('.')

from src.window import Window
from src.shapes import Line, Point, Cell

def main() -> None:
    win: Window = Window(800, 600)

    for i in range(16):
        c = Cell(10+(i*30)+((i-1)*10), 50, 10+((i+1)*30)+((i-1)*10), 100, win)
        c.has_left_wall = (i & 0b0001)
        c.has_right_wall = ((i & 0b0010) >> 1)
        c.has_top_wall = ((i & 0b0100) >> 2)
        c.has_bottom_wall = ((i & 0b1000) >> 3)
        c.draw()
    
    win.wait_for_close()

if __name__ == '__main__':
    main()