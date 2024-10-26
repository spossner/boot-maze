from window import Window
from maze import Maze
import random

BOOL = (True, False)
def randBool():
    return random.choice(BOOL)


if __name__ == "__main__":
    win = Window(800, 600)

    maze = Maze(10, 10, 16, 16, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    print("MAZE DONE")
    
    win.wait_for_close()
