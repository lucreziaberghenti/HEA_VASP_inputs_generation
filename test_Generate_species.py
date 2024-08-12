import unittest
from functions import Generate_species

class TestGenerateSpeciesFunction(unittest.TestCase):

    def test_generate_species(self):
        # Test con una matrice 2x2x2 con valori da 1 a 5
        conf = [
            [[1, 2], [3, 4]],
            [[5, 1], [2, 3]]
        ]
        expected_output = ['Co', 'Cr', 'Fe', 'Mn', 'Ni', 'Co', 'Cr', 'Fe']
        self.assertEqual(Generate_species(conf), expected_output)

        # Test con una matrice 1x2x2 con valori da 1 a 3
        conf = [
            [[1, 2], [3, 1]]
        ]
        expected_output = ['Co', 'Cr', 'Fe', 'Co']
        self.assertEqual(Generate_species(conf), expected_output)
        
        # Test con una matrice 1x1x1 con un solo valore
        conf = [
            [[5]]
        ]
        expected_output = ['Ni']
        self.assertEqual(Generate_species(conf), expected_output)

        # Test con valori che non sono mappati
        conf = [
            [[0]]
        ]
        expected_output = ['error']
        self.assertEqual(Generate_species(conf), expected_output)

if __name__ == '__main__':
    unittest.main()