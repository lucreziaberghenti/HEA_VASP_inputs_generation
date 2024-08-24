import unittest
import numpy as np
from functions import newConf
from functions import Equivalent

#fix a random seed to run tests
seed=0

class Test_newConf(unittest.TestCase):
    """
    Unit test class for the newConf function.
    """

    def test_generate_new_conf_dimensions(self):
        """
        given: - n which is the np array [1,1,2,2,3,3] that contains the elements of the new configuration to generate 
               - the desired dimensions of the new configuration (1,1,6)
        when: calling newConf
        expected output: the generated conf is a ndarry of dimensions (1,1,6)
        """
        saved = []
        n=np.repeat(np.arange(1,4), 2)
        conf = newConf(saved, 1, 1, 6, n, seed)
        self.assertEqual(conf.shape, (1, 1, 6), "Wrong dimensions")
   
    def test_generate_new_conf_distribution(self):
        """
        given: n which is the np array [1,1,2,2,3,3] that contains the elements of the new configuration to generate
        when: calling newConf
        expected output: the generated conf the correct distribution of elements (1,2,3 are repeated 2 times each)
        """
        saved = []
        n=np.repeat(np.arange(1,4), 2)
        conf = newConf(saved, 1, 1, 6, n, seed)
       
        #array of ripetions
        rip_expected = np.array([2,2,2])
        rip_generated = np.array([np.sum(conf == i) for i in range(1,4)])
       
        self.assertTrue(np.array_equal(rip_generated, rip_expected), "Wrong distribution of elements")

    def test_generate_non_equivalent_conf(self):
        """
        given:  - n which is the np array [1,1,2,2,3,3] that contains the elements of the new configuration to generate
                - saved variable having only one element: np array [1,2,1,2,3,3]
                - the desired dimensions of the new configuration (1,1,6)
        when: calling newConf
        expected output: the generated conf is a ndarry of dimensions (1,1,6) non-equivalent to the one saved
        """
        saved = [np.array([[[1,2,1,2,3,3]]])]
        n=np.repeat(np.arange(1,4), 2)
        conf = newConf(saved, 1, 1, 6, n, seed)
       
        self.assertFalse(Equivalent(conf, saved), "Generated configuration is equivalent to one already saved")

    def test_generate_unique_conf(self):
        """
        given:  - n which is the np array [1,1,2,2,3,3] that contains the elements of the new configuration to generate
                - the desired dimensions of the new configuration (1,1,6)
        when: calling newConf 2 different times
        expected output: the generated configurations conf1 and conf2 are non-equivalent ndarrys of dimensions (1,1,6)
        """
        saved = []
        n=np.repeat(np.arange(1,4), 2)
        conf1 = newConf(saved, 1, 1, 6, n, seed)
        saved.append(conf1)
        conf2 = newConf(saved, 1, 1, 6, n, seed)
       
        self.assertFalse(np.array_equal(conf1, conf2), "The two saved configurations should be different")


if __name__ == '__main__':
    """
    Executes the test cases when the script is run directly.
    """
    unittest.main()