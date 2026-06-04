# shapestest.py

import unittest
from areacircle import circle_area, square_area, rectangle_area, triangle_area


class TestAreaFunctions(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(3), 28.26)

    def test_square_area(self):
        self.assertEqual(square_area(5), 25)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 7), 35)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 6), 15)


if __name__ == "__main__":
    unittest.main()