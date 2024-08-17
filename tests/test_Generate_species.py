import unittest
import numpy as np
from functions import Generate_species

class TestGenerateSpeciesFunction(unittest.TestCase):

    def test_generate_species(self):

        #Test with matrix 2x2x2 having values from 1 to 5
        conf = np.array([
            [[1, 2], [3, 4]],
            [[5, 1], [2, 3]]
        ], dtype=int)

        expected_output = ['Co', 'Cr', 'Fe', 'Mn', 'Ni', 'Co', 'Cr', 'Fe']
        self.assertEqual(Generate_species(conf), expected_output)

        #Test with matrix 1x2x2 having values from 1 to 3
        conf = np.array([
            [[1, 2], [3, 1]]
        ], dtype=int)

        expected_output = ['Co', 'Cr', 'Fe', 'Co']
        self.assertEqual(Generate_species(conf), expected_output)
        
        # Test with a matrix 1x1x1 having only one value
        conf = np.array([
            [[5]]
        ], dtype=int)

        expected_output = ['Ni']
        self.assertEqual(Generate_species(conf), expected_output)

        #Test with non mapped values
        conf = np.array([
            [[0]]
        ], dtype=int)

        expected_output = ['error']
        self.assertEqual(Generate_species(conf), expected_output)

# if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()