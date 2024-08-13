import unittest
import numpy as np
from functions import Find

class TestFindFunction(unittest.TestCase):
    
    def test_find_positive(self):
        # Positive case: m2 is a sub-matrix of m1
        m1 = np.array([[[1, 2, 4, 1],
                        [4, 1, 2, 3],
                        [5, 4, 3, 5],
                        [5, 1, 5, 2]],

                       [[1, 4, 2, 4],
                        [1, 3, 5, 1],
                        [5, 4, 3, 3],
                        [5, 1, 5, 2]]], dtype=int)
        
        m2 = np.array([[[1, 2],
                        [4, 1]]], dtype=int)
        
        result = Find(m1, m2)
        self.assertEqual(result, 1)

    def test_find_negative(self):
        # Negative case: m2 is not a sub-matrix of m1
        m1 = np.array([[[1, 2, 4, 1],
                        [4, 1, 2, 3],
                        [5, 4, 3, 5],
                        [5, 1, 5, 2]],

                       [[1, 4, 2, 4],
                        [1, 3, 5, 1],
                        [5, 4, 3, 3],
                        [5, 1, 5, 2]]], dtype=int)
        
        m2 = np.array([[[2, 2],
                        [2, 2]]], dtype=int)
        
        result = Find(m1, m2)
        self.assertEqual(result, 0)

    
    def test_find_empty_m2(self):
        # Edge case: m2 is an empty matrix
        m1 = np.array([[[1, 2, 4, 1],
                        [4, 1, 2, 3],
                        [5, 4, 3, 5],
                        [5, 1, 5, 2]],

                       [[1, 4, 2, 4],
                        [1, 3, 5, 1],
                        [5, 4, 3, 3],
                        [5, 1, 5, 2]]], dtype=int)
        
        m2 = np.array([[[ ]]], dtype=int)
        
        result = Find(m1, m2)
        self.assertEqual(result, 0)
    
#if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()