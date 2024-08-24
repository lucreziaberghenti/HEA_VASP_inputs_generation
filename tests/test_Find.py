import unittest
import numpy as np
from functions import Find

class TestFindFunction(unittest.TestCase):
    """Unit tests for the Find function."""

    def test_find_positive(self):
        """
        given: a matrix m2 which is a sub-matrix of m1
        when: calling Find
        expected output: positive result (1) since there exists a sub-matrix of m1 equal to m2
        """
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
        """
        given: a matrix m2 which is not a sub-matrix of m1
        when: calling Find
        expected output: negative result (0) since there not exists a sub-matrix of m1 equal to m2
        """
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
        """
        given: m2 which is an empty matrix and m1 a generic matrix
        when: calling Find
        expected output: a negative result (0) since an empty matrix cannot be a sub-matrix of any matrix
        
        """
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
   
# if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()

