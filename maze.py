from config import *
from geo import *
from cell import Cell, Walls
import time
import random
import collections
from enum import Enum
import collections

DIRECTION = [(0,1),(0,-1),(1,0),(-1,0)]

class Maze:
    def __init__(self, x, y, nums_rows, num_cols, win = None, seed = None) -> None:
        self.x = x
        self.y = y
        self.num_rows = nums_rows
        self.num_cols = num_cols
        self._cells = []
        self.win = win
        if seed:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for x in range(self.num_cols):
            col = []
            for y in range(self.num_rows):
                p1 = Point(self.x + x * CELL_WIDTH, self.y + y * CELL_HEIGHT)
                p2 = p1.translate(CELL_WIDTH, CELL_HEIGHT)
                col.append(Cell(p1, p2, Walls(), self.win))
            self._cells.append(col)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j, highlight = False):
        c = self._cells[i][j]
        c.draw(highlight)
        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.01)

    def _break_entrance_and_exit(self):
        top_left = self._cells[0][0]
        top_left.walls.top = False
        self._draw_cell(0,0)
        bottom_right = self._cells[-1][-1]
        bottom_right.walls.bottom = False
        self._draw_cell(-1,-1)

    def _break_wall(self, i,j, dx,dy):
        ni, nj = i+dx, j+dy
        if dx == 1:
            self._cells[i][j].walls.right = False
            self._cells[ni][nj].walls.left = False
        elif dx == -1:
            self._cells[i][j].walls.left = False
            self._cells[ni][nj].walls.right = False
        elif dy == 1:
            self._cells[i][j].walls.bottom = False
            self._cells[ni][nj].walls.top = False
        elif dy == -1:
            self._cells[i][j].walls.top = False
            self._cells[ni][nj].walls.bottom = False

    def _break_walls_r(self, i, j):
        c = self._cells[i][j]
        c.visited = True
        while True:
            adjacent = []
            for dx, dy in DIRECTION:
                ni = i + dx
                nj = j + dy
                if ni < 0 or nj < 0 or ni >= self.num_cols or nj >= self.num_rows:
                    continue
                new_cell = self._cells[ni][nj]
                if new_cell.visited:
                    continue
                adjacent.append((dx, dy))
            if not adjacent:
                self._draw_cell(i,j) # no more neighbours to visit
                break

            dx, dy = random.choice(adjacent)
            self._break_wall(i,j,dx,dy)
            self._break_walls_r(i+dx,j+dy)
