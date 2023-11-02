import unittest
from rectangle import Rectangle as rec 

    # TODO: 1. Prepare example Rectangle data
    # TODO: 2. Verify implemented methods

class TestRectangleMethods(unittest.TestCase):
    
    def test_contains1(self):
        
        rect1 = rec(2, 3, 5, 4)
        rect2 = rec(3, 4, 2, 2)

        self.assertTrue(rect1.contains(rect2))
         
    def test_contains2(self):
        
        rect1 = rec(-2, -3, 7, 3)
        rect2 = rec(-3, 4, -2, 2)

        self.assertFalse(rect1.contains(rect2))
         
    def test_contains3(self):
        
        rect1 = rec(7, -3, 1, -4)
        rect2 = rec(9, 5, 6, -2)

        self.assertFalse(rect1.contains(rect2))
         
    def test_contains4(self):
        
        rect1 = rec(4, 8, 6, -1)
        rect2 = rec(-3, -4, 8, -5)

        self.assertFalse(rect1.contains(rect2))
         
    def test_contains5(self):
        
        rect1 = rec(4, 2, 7, 4)
        rect2 = rec(5, 5, 5, -2)

        self.assertTrue(rect1.contains(rect2))
             
    def test_contains6(self):
        
        rect1 = rec(-2, -2, 7, 8)
        rect2 = rec(4, 5, -5, -2)

        self.assertTrue(rect1.contains(rect2))
             
    def test_contains7(self):
        
        rect1 = rec(7, 2, -7, -4)
        rect2 = rec(8, 1, 1, -2)

        self.assertFalse(rect1.contains(rect2))
             
    def test_contains8(self):
        
        rect1 = rec(-6, -2, 6, 1)
        rect2 = rec(0, 0, -1, -1)

        self.assertTrue(rect1.contains(rect2))
             
    def test_contains9(self):
        
        rect1 = rec(3, -2, -7, -4)
        rect2 = rec(-3, -5, 3, 2)

        self.assertFalse(rect1.contains(rect2))
             
    def test_contains10(self):
        
        rect1 = rec(1, 1, 4, 5)
        rect2 = rec(2, 3, 2, 3)

        self.assertTrue(rect1.contains(rect2))

    def test_intersect1(self):
        
        rect1 = rec(2, 3, 5, 4)
        rect2 = rec(3, 4, 2, 2)

        self.assertTrue(rect1.intersect(rect2))
        
    def test_intersect2(self):
        
        rect1 = rec(-2, 3, 5, 4)
        rect2 = rec(5, 4, 2, 2)

        self.assertFalse(rect1.intersect(rect2))
        
    def test_intersect3(self):
        
        rect1 = rec(3, 3, 5, 4)
        rect2 = rec(4, 6, 2, 2)

        self.assertTrue(rect1.intersect(rect2))
        
    def test_intersect4(self):
        
        rect1 = rec(-5, -3, -5, -4)
        rect2 = rec(4, 1, 1, 2)

        self.assertFalse(rect1.intersect(rect2))
        
    def test_intersect5(self):
        
        rect1 = rec(-4, -1, 9, 2)
        rect2 = rec(1, 0, 2, 2)

        self.assertTrue(rect1.intersect(rect2))
        
    def test_intersect6(self):
        
        rect1 = rec(5, 5, 2, 1)
        rect2 = rec(3, 4, 2, 2)

        self.assertFalse(rect1.intersect(rect2))
        
    def test_intersect7(self):
        
        rect1 = rec(1, 5, 7, 3)
        rect2 = rec(2, 7, 9, 2)

        self.assertTrue(rect1.intersect(rect2))
        
    def test_intersect8(self):
        
        rect1 = rec(-2, -2, 2, 2)
        rect2 = rec(0, 0, 1, 2)

        self.assertFalse(rect1.intersect(rect2))
        
    def test_intersect9(self):
        
        rect1 = rec(-3, 0, 9, 6)
        rect2 = rec(1, 2, 7, 3)

        self.assertTrue(rect1.intersect(rect2))
        
    def test_intersect10(self):
        
        rect1 = rec(1, 5, 5, 4)
        rect2 = rec(3, 4, 4, 1)

        self.assertFalse(rect1.intersect(rect2))
        
if __name__ == '__main__':
    unittest.main()   