import unittest
import numpy as np
from functions import Equivalent

class TestEquivalent(unittest.TestCase):
    """Unit tests for the Equivalent function."""

    def test_equivalent_identical(self):
        """
        Test case where the configuration 'conf' is identical to one of the elements
        in the 'saved' array.
        """
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=int)
        saved = np.array([[[[1, 2], [3, 4]], [[1, 2], [3, 4]]]], dtype=int)

        self.assertEqual(Equivalent(conf, saved), 1)

    def test_equivalent_different(self):
        """
        Test case where the configuration 'conf' is different from all the elements
        in the 'saved' array.
        """
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 5]]], dtype=int)
        saved = np.array([[[[1, 2], [3, 4]], [[1, 2], [3, 4]]]], dtype=int)

        self.assertEqual(Equivalent(conf, saved), 0)

    def test_equivalent_no_saved(self):
        """
        Test case where there are no saved configurations (i.e., 'saved' is an empty array).
        """
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=int)
        saved = np.array([], dtype=int).reshape(0, 0, 0, 0)

        self.assertEqual(Equivalent(conf, saved), 0)

    def test_equivalent_equivalent_transformation(self):
        """
        Test case where the configuration 'conf' is equivalent to one of the elements
        in the 'saved' array after applying a transformation (e.g., translation).
        """
        conf = np.array([[[3, 4], [1, 2]], [[3, 4], [1, 2]]], dtype=int)
        saved = np.array([[[[1, 2], [3, 4]], [[1, 2], [3, 4]]]], dtype=int)
       
        self.assertEqual(Equivalent(conf, saved), 1)

# if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()