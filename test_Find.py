import unittest
import numpy as np

class TestFindFunction(unittest.TestCase):
    
    def test_find_positive(self):
        # Positive case: m2 is a sub-matrix of m1
        m1 = np.array([
            [[ 1,  2,  3,  4], [ 5,  6,  7,  8], [ 9, 10, 11, 12]],
            [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
        ])
        m2 = np.array([
            [ 6,  7], 
            [18, 19]
        ])
        result = Find(m1, m2)
        self.assertEqual(result, 1)

    def test_find_negative(self):
        # Negative case: m2 is not a sub-matrix of m1
        m1 = np.array([
            [[ 1,  2,  3,  4], [ 5,  6,  7,  8], [ 9, 10, 11, 12]],
            [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
        ])
        m2 = np.array([
            [ 6,  8], 
            [18, 21]
        ])
        result = Find(m1, m2)
        self.assertEqual(result, 0)

    
    def test_find_empty_m2(self):
        # Edge case: m2 is an empty matrix
        m1 = np.array([
            [[ 1,  2,  3,  4], [ 5,  6,  7,  8], [ 9, 10, 11, 12]],
            [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
        ])
        m2 = np.array([[]])
        result = Find(m1, m2)
        self.assertEqual(result, 0)
    
    def test_find_empty_m1(self):
        # Edge case: m1 is an empty matrix
        m1 = np.array([[]])
        m2 = np.array([
            [1, 2], 
            [3, 4]
        ])
        result = Find(m1, m2)
        self.assertEqual(result, 0)
    
#if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()