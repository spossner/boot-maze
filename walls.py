class Walls:
    def __init__(self, top = True, right = True, bottom = True, left = True):
         self.top = top
         self.right = right
         self.bottom = bottom
         self.left = left

    def as_tuple(self):
        return (self.top, self.right, self.bottom, self.left)

    def __eq__(self, other):
        if isinstance(other, Walls):
            return self.top == other.top and self.right == other.right and self.bottom == other.bottom and self.left == other.left
        if isinstance(other, tuple):
            return self.as_tuple() == other
        return False
         
