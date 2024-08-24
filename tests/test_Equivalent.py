import unittest
import numpy as np
from functions import Equivalent

class TestEquivalent(unittest.TestCase):
    """Unit tests for the Equivalent function."""

    def test_equivalent_identical(self):
        """
        given: a configuration equal to the one already saved
        when: calling Equivalent function
        expected output: Equivalent returns 1 since the two matrices are equal

        """
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=int)
        saved = np.array([[[[1, 2], [3, 4]], [[1, 2], [3, 4]]]], dtype=int)

        self.assertEqual(Equivalent(conf, saved), 1)

    def test_equivalent_different(self):
        """
        given: a configuration non-equivalent to the one already saved
        when: calling Equivalent function
        expected output: Equivalent returns 0 since the two matrices are not equivalent
        
        """
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 5]]], dtype=int)
        saved = np.array([[[[1, 2], [3, 4]], [[1, 2], [3, 4]]]], dtype=int)

        self.assertEqual(Equivalent(conf, saved), 0)

    def test_equivalent_no_saved(self):
        """
        given: a configuration and saved empty
        when: calling Equivalent function
        expected output: Equivalent returns 0 since there are no saved matrices
        
        """
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=int)
        saved = np.array([], dtype=int).reshape(0, 0, 0, 0)

        self.assertEqual(Equivalent(conf, saved), 0)

    def test_equivalent_equivalent_transformation(self):
        """
        given: a configuration equivalent by transaltion to the one already saved
        when: calling Equivalent function
        expected output: Equivalent returns 1 since the two matrices are equivalent

        """
        conf = np.array([[[3, 4], [1, 2]], [[3, 4], [1, 2]]], dtype=int)
        saved = np.array([[[[1, 2], [3, 4]], [[1, 2], [3, 4]]]], dtype=int)
       
        self.assertEqual(Equivalent(conf, saved), 1)

# if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()