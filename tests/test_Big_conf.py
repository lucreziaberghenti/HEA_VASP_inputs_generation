import unittest
import numpy as np
from functions import Big_conf

class TestBigConf(unittest.TestCase):
    """
    Unit tests for the Big_conf function.
    """

    def test_big_conf_basic(self):
        """
        Test Big_conf with a 1x1x1 matrix.
        Verifies that a single element is expanded correctly.
        """
        conf = np.array([[[1]]], dtype=int)
        expected_output = np.array([[[1, 1], [1, 1]], [[1, 1], [1, 1]]], dtype=int)
        output = Big_conf(conf)

        np.testing.assert_array_equal(output, expected_output)

    def test_big_conf_standard(self):
        """
        Test Big_conf with a 2x2x2 matrix.
        Verifies that a standard matrix is expanded correctly.
        """
        conf = np.array([[[1, 2], [3, 4]], [[5, 1], [2, 3]]], dtype=int)
        expected_output = np.array([
            [[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]],
            [[5, 1, 5, 1], [2, 3, 2, 3], [5, 1, 5, 1], [2, 3, 2, 3]],
            [[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]],
            [[5, 1, 5, 1], [2, 3, 2, 3], [5, 1, 5, 1], [2, 3, 2, 3]]
        ], dtype=int)
        output = Big_conf(conf)

        np.testing.assert_array_equal(output, expected_output)

    def test_big_conf_empty(self):
        """
        Test Big_conf with an empty matrix.
        Verifies that an empty matrix remains empty after the function is applied.
        """
        conf = np.array([], dtype=int).reshape(0, 0, 0)
        expected_output = np.array([], dtype=int).reshape(0, 0, 0)
        output = Big_conf(conf)

        np.testing.assert_array_equal(output, expected_output)

    def test_big_conf_single_layer(self):
        """
        Test Big_conf with a single 2x2 slice.
        Verifies that a single slice is expanded correctly.
        """
        conf = np.array([[[1, 2], [3, 4]]], dtype=int)
        expected_output = np.array([
            [[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]],
            [[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]]
        ], dtype=int)
        output = Big_conf(conf)

        np.testing.assert_array_equal(output, expected_output)

# if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()