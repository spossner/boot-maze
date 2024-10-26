import unittest
from maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.num_cols = 12
        self.num_rows = 10
        self.maze = Maze(0,0,self.num_rows,self.num_cols)
        
    def test_maze_create(self):
        self.assertEqual(len(self.maze._cells), self.num_cols)
        self.assertEqual(len(self.maze._cells[0]), self.num_rows)

    def test_break_entry_and_exit(self):
        self.maze._break_entrance_and_exit()
        self.assertEqual(self.maze._cells[0][0].walls, (False,True,True,True))
        self.assertEqual(self.maze._cells[-1][-1].walls, (True,True,False,True))

if __name__ == '__main__':
    unittest.main()
