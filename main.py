from window import Window
from maze import Maze
import random

BOOL = (True, False)
def randBool():
    return random.choice(BOOL)


if __name__ == "__main__":
    win = Window(800, 600)

    maze = Maze(10, 10, 16, 16, win)
    maze.break_walls()

    maze.solve()
    
    win.wait_for_close()
