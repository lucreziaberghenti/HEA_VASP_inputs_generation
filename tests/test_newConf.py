import unittest
import numpy as np
from functions import newConf
from functions import Equivalent

class Test_newConf(unittest.TestCase):

    # test check on dimensions of generated conf
    def test_generate_new_conf_dimensions(self):
        
        saved = []
        conf = newConf(saved)
        self.assertEqual(conf.shape, (3, 4, 5), "Wrong dimensions")
    
    # test on generated number of ripetions (distribution) for each element 1,2,3,4,5
    def test_generate_new_conf_distribution(self):
        
        saved = []
        conf = newConf(saved)
        
        n_expected = np.array([12, 12, 12, 12, 12])
        n_generated = np.array([np.sum(conf == i) for i in range(1, 6)])
        
        self.assertTrue(np.array_equal(n_generated, n_expected), "Wrong distribution of elements")


    # test to check that the new configuration is not equivalent to the one already saved
    def test_generate_non_equivalent_conf(self):
        
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

    # test to check that different calls of newConf generate different configurations
    def test_generate_unique_conf(self):
        
        saved = []
        conf1 = newConf(saved)
        saved.append(conf1)
        conf2 = newConf(saved)
        
        self.assertFalse(np.array_equal(conf1, conf2), "The two saved configurations should be different")

#if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()