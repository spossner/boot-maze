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
                self._cells[i][j].draw()

    def _draw_cell(self, i, j):
        c = self._cells[i][j]
        c.draw()
        # self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.03)

    def _break_entrance_and_exit(self):
        top_left = self._cells[0][0]
        top_left.walls.top = False
        self._draw_cell(0,0)
        bottom_right = self._cells[-1][-1]
        bottom_right.walls.bottom = False
        self._draw_cell(-1,-1)

    def get_wall(self, i, j, dx, dy) -> bool:
        if dx == 1:
            return self._cells[i][j].walls.right
        if dx == -1:
            return self._cells[i][j].walls.left
        if dy == 1:
            return self._cells[i][j].walls.bottom
        if dy == -1:
            return self._cells[i][j].walls.top
        

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

    def break_walls(self):
        self._break_entrance_and_exit()
        self._break_walls_r(0,0,set())

    def _break_walls_r(self, i, j, seen):
        c = self._cells[i][j]
        seen.add((i,j))
        while True:
            adjacent = []
            for dx, dy in DIRECTION:
                ni = i + dx
                nj = j + dy
                if ni < 0 or nj < 0 or ni >= self.num_cols or nj >= self.num_rows:
                    continue
                if (ni,nj) in seen:
                    continue
                adjacent.append((dx, dy))
            if not adjacent:
                self._draw_cell(i,j) # no more neighbours to visit
                break

            dx, dy = random.choice(adjacent)
            self._break_wall(i,j,dx,dy)
            self._break_walls_r(i+dx,j+dy,seen)

    def solve(self) -> bool:
        return self.solve_r(0,0,set())

    def solve_r(self, i, j, seen):
        seen.add((i,j))
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True # found exit!
        c1 = self._cells[i][j]
        for dx, dy in DIRECTION:
            ni = i + dx
            nj = j + dy
            if ni < 0 or nj < 0 or ni >= self.num_cols or nj >= self.num_rows:
                continue
            if (ni,nj) in seen:
                continue
            if not self.get_wall(i,j,dx,dy):
                c2 = self._cells[ni][nj]
                self.win.draw_move(c1,c2)
                if self.should_redraw():
                    self._animate()
                if self.solve_r(ni,nj,seen):
                    return True
                self.win.draw_move(c1,c2,True)
                if self.should_redraw():
                    self._animate()
                
        return False
    
    def should_redraw(self) -> bool:
        return random.randint(0,100) > 70

    def draw_path(self, path):
        for i in range(len(path)-1):
            x1, y1 = path[i]
            x2, y2 = path[i+1]
            c1 = self._cells[x1][y1]
            c2 = self._cells[x2][y2]
            self.win.draw_move(c1, c2)
