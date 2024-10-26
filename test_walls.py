import unittest
from walls import Walls

class TestWalls(unittest.TestCase):
    def test_eq(self):
        w = Walls()
        self.assertEqual(w, (True, True, True, True))
        self.assertNotEqual(w, True)
        self.assertEqual(w, Walls())
        self.assertNotEqual(w, Walls(False,True,False,True))
