import sys
sys.path.append('.')

from src.window import Window
from src.shapes import Line, Point

def main() -> None:
    win: Window = Window(800, 600)
    l: Line = Line(Point(200, 200), Point(600, 200))
    
    win.draw_line(l, 'red')
    win.wait_for_close()

if __name__ == '__main__':
    main()