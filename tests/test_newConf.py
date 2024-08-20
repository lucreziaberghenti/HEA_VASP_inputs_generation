import unittest
import numpy as np
from functions import newConf
from functions import Equivalent

class Test_newConf(unittest.TestCase):
    """
    Unit test class for the newConf function.
    """

    def test_generate_new_conf_dimensions(self):
        """
        Test to check that the generated configuration has the correct dimensions (3, 4, 5).
        """
        saved = []
        conf = newConf(saved)
        self.assertEqual(conf.shape, (3, 4, 5), "Wrong dimensions")
   
    def test_generate_new_conf_distribution(self):
        """
        Test to verify that the generated configuration has the correct distribution of elements (1, 2, 3, 4, 5),
        with 12 occurrences of each element.
        """
        saved = []
        conf = newConf(saved)
       
        n_expected = np.array([12, 12, 12, 12, 12])
        n_generated = np.array([np.sum(conf == i) for i in range(1, 6)])
       
        self.assertTrue(np.array_equal(n_generated, n_expected), "Wrong distribution of elements")

    def test_generate_non_equivalent_conf(self):
        """
        Test to ensure that the generated configuration is not equivalent
        to any of the configurations already saved.
        """
        saved = [np.array([[[1, 1, 2, 2, 3],
                            [1, 2, 3, 4, 5],
                            [1, 2, 3, 4, 5],
                            [1, 2, 3, 4, 5]],
                           [[1, 1, 2, 2, 3],
                            [1, 2, 3, 4, 5],
                            [1, 2, 3, 4, 5],
                            [1, 2, 3, 4, 5]],
                           [[1, 1, 2, 2, 3],
                            [1, 2, 3, 4, 5],
                            [1, 2, 3, 4, 5],
                            [1, 2, 3, 4, 5]]])]
       
        conf = newConf(saved)
       
        self.assertFalse(Equivalent(conf, saved), "Generated configuration is equivalent to one already saved")

    def test_generate_unique_conf(self):
        """
        Test to check that multiple calls to newConf generate different configurations.
        """
        saved = []
        conf1 = newConf(saved)
        saved.append(conf1)
        conf2 = newConf(saved)
       
        self.assertFalse(np.array_equal(conf1, conf2), "The two saved configurations should be different")

if __name__ == '__main__':
    """
    Executes the test cases when the script is run directly.
    """
    unittest.main()