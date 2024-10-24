from tkinter import Tk, BOTH, Canvas
from geo import Point, Line
import time

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Hello, world")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=800, height=height)
        self.canvas.pack(fill="both")
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            time.sleep(0.016)

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)

if __name__ == "__main__":
    win = Window(800, 600)
    line = Line(Point(12,12), Point(600,200))
    win.draw_line(line, "#ec7bcb")
    win.wait_for_close()
