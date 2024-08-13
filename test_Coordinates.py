import unittest
import numpy as np
from ase.build import fcc111

class TestCoordinates(unittest.TestCase):

    def test_coordinates_shape(self):
        # Test if the function returns an array of dim (60, 3)
        coords = Coordinates()
        self.assertEqual(coords.shape, (60, 3))

    def test_atom_positions(self):
        # Test if the first atomic positions are the expected of ones of Ni fcc(111)
        expected_positions = np.array([
            [0.0, 0.0, 0.0],
            [1.8, 1.03923048, 0.0],
            [3.6, 2.07846097, 0.0],
            [0.0, 2.07846097, 2.54950976],
            [1.8, 3.11769145, 2.54950976]
            # ... possible to add other positions ...
        ])
        
        coords = Coordinates()
        
        # Verify that the first n positions are equal to the exected ones (with a certain tolerance)
        np.testing.assert_almost_equal(coords[:len(expected_positions)], expected_positions, decimal=6)
    
    def test_fcc_properties(self):
        # Test of few properties of fcc lattice
        coords = Coordinates()
        d = np.linalg.norm(coords[0] - coords[1])  # distance between nearest negihbours
        expected_d = 3.6 / np.sqrt(2)
        self.assertAlmostEqual(d, expected_d, places=6)

        # Test on angle between base vectors
        v1 = coords[1] - coords[0]
        v2 = coords[2] - coords[0]
        angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
        self.assertAlmostEqual(angle, 120 * np.pi / 180, places=6)

if _name_ == '_main_':
    unittest.main()