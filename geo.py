from tkinter import Canvas

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"
    
    def translate_y(self, offset: float):
        return Point(self.x,self.y+offset)

    def translate_x(self, offset: float):
        return Point(self.x+offset,self.y)
    
    def translate(self, dx: float, dy: float):
        return Point(self.x+dx,self.y+dy)
    

class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)
