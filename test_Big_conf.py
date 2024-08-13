import unittest
import numpy as np

class TestBigConf(unittest.TestCase):
    # Test with a 1x1x1 matrix
    def test_big_conf_basic(self):

        conf = np.array([[[1]]], dtype=int)
        expected_output = np.array([[[1, 1], [1, 1]], [[1, 1], [1, 1]]], dtype=int)
        output = Big_conf(conf)

        np.testing.assert_array_equal(output, expected_output)

    # Test with a 2x2x2 matrix
    def test_big_conf_standard(self):
        
        conf = np.array([[[1, 2], [3, 4]], [[5, 1], [2, 3]]], dtype=int)
        expected_output = np.array([
            [[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]],
            [[5, 1, 5, 1], [2, 3, 2, 3], [5, 1, 5, 1], [2, 3, 2, 3]],
            [[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]],
            [[5, 1, 5, 1], [2, 3, 2, 3], [5, 1, 5, 1], [2, 3, 2, 3]]
        ], dtype=int)
        output = Big_conf(conf)

        np.testing.assert_array_equal(output, expected_output)

    # Test with empty matrix
    def test_big_conf_empty(self):
        
        conf = np.array([], dtype=int).reshape(0, 0, 0)
        expected_output = np.array([], dtype=int).reshape(0, 0, 0)
        output = Big_conf(conf)

        np.testing.assert_array_equal(output, expected_output)

    # Test with a single slice 2x2
    def test_big_conf_single_layer(self):
        
        conf = np.array([[[1, 2], [3, 4]]], dtype=int)
        expected_output = np.array([
            [[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]],
            [[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]]
        ], dtype=int)
        output = Big_conf(conf)

        np.testing.assert_array_equal(output, expected_output)

#if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()