from tkinter import Tk, BOTH, Canvas
import time
from geo import Point,Line
from cell import Cell
from config import *

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Hello, world")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=800, height=height, background=BACKGROUND)
        self.canvas.pack(fill="both")
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            time.sleep(0.0167)

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)

    def draw_rect(self, p1: Point, p2: Point, fill_color: str) -> None:
        self.canvas.create_rectangle(p1.x, p1.y, p2.x, p2.y, fill=fill_color)

    def draw_move(self, cell_1: Cell, cell_2: Cell, undo: bool = False) -> None:
        self.draw_line(Line(cell_1.get_center(), cell_2.get_center()), UNDO_COLOR if undo else MOVE_COLOR) 
