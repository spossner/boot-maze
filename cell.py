from geo import Point, Line
import collections
from config import *
from walls import Walls


class Cell:
    def __init__(self, p1: Point, p2: Point, walls: Walls, win = None) -> None:
        self.p1 = p1
        self.p2 = p2
        self.walls = walls
        self.win = win
        self.visited = False

    def get_wall_color(self, wall_present: bool) -> str:
        return COLOR if wall_present else BACKGROUND

    def draw(self, highlight=False):
        if not self.win:
            return
        
        top_left = self.p1
        top_right = self.p1.translate_x(CELL_WIDTH)
        bottom_left = self.p2.translate_x(-CELL_WIDTH)
        bottom_right = self.p2

        if highlight:
            self.win.draw_rect(top_left, bottom_right, HIGHLIGHT_COLOR)

        self.win.draw_line(Line(top_left, bottom_left), fill_color=self.get_wall_color(self.walls.left))
        self.win.draw_line(Line(top_right, bottom_right), fill_color=self.get_wall_color(self.walls.right))
        self.win.draw_line(Line(top_left, top_right), fill_color=self.get_wall_color(self.walls.top))
        self.win.draw_line(Line(bottom_left, bottom_right), fill_color=self.get_wall_color(self.walls.bottom))

    def get_center(self) -> Point:
        return Point((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)
