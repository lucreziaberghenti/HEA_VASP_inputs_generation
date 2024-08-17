import unittest
import numpy as np
from ase.build import fcc111
from functions import Coordinates

class TestCoordinates(unittest.TestCase):

    # test if the function returns an array of dim (60, 3)
    def test_coordinates_shape(self):
        
        coords = Coordinates()
        self.assertEqual(coords.shape, (60, 3))

    # test if the first atomic positions are the expected of ones of Ni fcc(111)
    def test_atom_positions(self):
        
        expected_positions = np.array([
            [ 1.27279221,  0.73484692,  0.        ],
            [ 3.81837662,  0.73484692,  0.        ],
            [ 6.36396103,  0.73484692,  0.        ],
            [ 8.90954544,  0.73484692,  0.        ],
            [11.45512986,  0.73484692,  0.        ],
            [ 0.         , 2.93938769,  0.        ]
            # ... possible to add other positions ...
        ])
        
        coords = Coordinates()
        
        # Verify that the first n positions are equal to the exected ones (with a certain tolerance)
        np.testing.assert_almost_equal(coords[:len(expected_positions)], expected_positions, decimal=6)
    
    # test of few properties of fcc lattice
    def test_fcc_properties(self):
        
        coords = Coordinates()
        d = np.linalg.norm(coords[0] - coords[1])  # distance between nearest negihbours
        expected_d = 3.6 / np.sqrt(2)
        self.assertAlmostEqual(d, expected_d, places=6)

        # test on angle between base vectors
        v1 = coords[1] - coords[0]
        v2 = coords[2] - coords[0]
        angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
        self.assertAlmostEqual(angle, 0, places=6)

# if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()