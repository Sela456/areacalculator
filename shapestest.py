import unittest

#Test for Circle
def test_area_circle(pi, radius):
    return 3.14 * radius ** 2

class TestAreaCircle(unittest.TestCase):

    def test_area_circle(self):
        self.assertEqual(test_area_circle(33.14,3) , 28.26)

if __name__ == '__main__':

    unittest.main()


#Test for Square
def test_area_square(length, lenth):
    return length * length

class TestAreaSquare(unittest.TestCase):

    def test_area_square(self):
        self.assertEqual(test_area_square(5,5), 25)

if __name__ == '__main__':
    unittest.main()


#Test for Rectangle
def test_area_rectangle(length, breadth):
    return length * breadth

class TestAreaRectangle(unittest.TestCase):

    def test_area_rectangle(self):
        self.assertEqual(test_area_rectangle(5,7), 35)

if __name__ == '__main__':
    unittest.main()


#Test fir Triangle
def test_area_triangle(length, breadth):
    return 0.5 * length * breadth

class AreaTestTriangle(unittest.TestCase):

    def test_area_triangle(self):
        self.assertEqual(test_area_triangle(5,6), 15)  

if __name__ == '__main__':
    unittest.main()          
        
        


    
    