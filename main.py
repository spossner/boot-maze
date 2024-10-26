from window import Window
from maze import Maze
import random
from config import *

BOOL = (True, False)
def randBool():
    return random.choice(BOOL)


if __name__ == "__main__":
    win = Window(WIDTH, HEIGHT)

    maze = Maze(5, 5, NUM_ROWS, NUM_COLS, win)
    maze.break_walls()

    maze.solve()
    
    win.wait_for_close()
