import unittest
import numpy as np
from functions import Generate_species

class TestGenerateSpeciesFunction(unittest.TestCase):
    """
    Unit test class for the Generate_species function.
    """

    def test_all_range(self):
        """
        input: 2x2x2 matrix of integers values ranging from 1 to 5
        what: apply Generate_species that maps each element of the matrix into a specific string
        expected output: a list of str
        
        """

        conf = np.array([
            [[1, 2], [3, 4]],
            [[5, 1], [2, 3]]
        ], dtype=int)

        expected_output = ['Co', 'Cr', 'Fe', 'Mn', 'Ni', 'Co', 'Cr', 'Fe']
        self.assertEqual(Generate_species(conf), expected_output)

    def test_part_of_range(self):
        """
        input: 1x2x2 matrix having values from 1 to 3
        what: apply Generate_species that maps each element of the matrix into a string
        expected output: a list of str

        """
 
        conf = np.array([
            [[1, 2], [3, 1]]
        ], dtype=int)

        expected_output = ['Co', 'Cr', 'Fe', 'Co']
        self.assertEqual(Generate_species(conf), expected_output)

    def single_value(self):   
        """
        input: 1x1x1 matrix having only one integer value in the range 1:5
        what: apply Generate_species that maps the element of the matrix into a string
        expected output: a list of one string element

        """

        conf = np.array([
            [[5]]
        ], dtype=int)

        expected_output = ['Ni']
        self.assertEqual(Generate_species(conf), expected_output)
        

    def test_non_mapped_values(self):
        """
        input: 1x1x1 matrix having only one integer value outside the range 1:5
        what: apply Generate_species that maps the element of the matrix into a string
        expected output: 'error'

        """

        conf = np.array([
            [[0]]
        ], dtype=int)

        expected_output = ['error']
        self.assertEqual(Generate_species(conf), expected_output)

# if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()