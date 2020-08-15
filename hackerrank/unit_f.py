import unittest
from hackerrank.min_subarray import minArray

class test(unittest.TestCase):
    def setUp(self):
        self.arr = [2, 3, 0, -1, 2, 0, 10]
        self.wind = 3

    def testing(self):
        self.assertEqual(minArray(self.arr, self.wind), (3, 10), "Wrong output")