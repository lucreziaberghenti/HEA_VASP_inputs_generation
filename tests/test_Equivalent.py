import unittest
import numpy as np
from functions import Equivalent

class TestEquivalent(unittest.TestCase):

    # test with conf equal to one of the elements of saved
    def test_equivalent_identical(self):
        
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=int)
        saved = np.array([[[[1, 2], [3, 4]], [[1, 2], [3, 4]]]], dtype=int)

        self.assertEqual(Equivalent(conf, saved), 1)

    # test with conf different to one of the elements of saved
    def test_equivalent_different(self):
        
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 5]]], dtype=int)
        saved = np.array([[[[1, 2], [3, 4]], [[1, 2], [3, 4]]]], dtype=int)

        self.assertEqual(Equivalent(conf, saved), 0)

    # test with no saved configurations
    def test_equivalent_no_saved(self):
        
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=int)
        saved = np.array([], dtype=int).reshape(0, 0, 0, 0)

        self.assertEqual(Equivalent(conf, saved), 0)

    # test with conf equivalent to the translation of one of the saved configurations 
    def test_equivalent_equivalent_transformation(self):
        
        conf = np.array([[[3, 4], [1, 2]], [[3, 4], [1, 2]]], dtype=int)
        saved = np.array([[[[1, 2], [3, 4]], [[1, 2], [3, 4]]]], dtype=int)
        
        self.assertEqual(Equivalent(conf, saved), 1)

# if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()