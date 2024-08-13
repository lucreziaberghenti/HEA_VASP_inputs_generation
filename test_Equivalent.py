import unittest
import numpy as np

class TestEquivalent(unittest.TestCase):
    def test_equivalent_identical(self):
        # Test con conf identico a una delle configurazioni salvate
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=int)
        saved = np.array([
            [[[1, 2], [3, 4]], [[1, 2], [3, 4]]]
        ], dtype=int)
        self.assertEqual(Equivalent(conf, saved), 1)

    def test_equivalent_different(self):
        # Test con conf diverso dalle configurazioni salvate
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 5]]], dtype=int)
        saved = np.array([
            [[[1, 2], [3, 4]], [[1, 2], [3, 4]]]
        ], dtype=int)
        self.assertEqual(Equivalent(conf, saved), 0)

    def test_equivalent_empty_saved(self):
        # Test con conf e saved vuoti
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=int)
        saved = np.array([], dtype=int).reshape(0, 0, 0, 0)
        self.assertEqual(Equivalent(conf, saved), 0)

    def test_equivalent_empty_conf(self):
        # Test con conf vuoto
        conf = np.array([], dtype=int).reshape(0, 0, 0)
        saved = np.array([
            [[[1, 2], [3, 4]], [[1, 2], [3, 4]]]
        ], dtype=int)
        self.assertEqual(Equivalent(conf, saved), 0)

    def test_equivalent_no_saved(self):
        # Test con conf e nessuna configurazione salvata
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=int)
        saved = np.array([], dtype=int).reshape(0, 0, 0, 0)
        self.assertEqual(Equivalent(conf, saved), 0)
        
    def test_equivalent_equivalent_transformation(self):
        # Test con conf equivalente a una delle configurazioni salvate con una traslazione
        conf = np.array([[[3, 4], [1, 2]], [[3, 4], [1, 2]]], dtype=int)
        saved = np.array([
            [[[1, 2], [3, 4]], [[1, 2], [3, 4]]]
        ], dtype=int)
        # Se la funzione non considera la traslazione come equivalente, aspettarsi 0
        self.assertEqual(Equivalent(conf, saved), 0)
    
    def test_equivalent_larger_saved(self):
        # Test con una configurazione salvata più grande
        conf = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]], dtype=int)
        saved = np.array([
            [[[1, 2, 3], [4, 1, 2], [3, 4, 1]], [[2, 3, 4], [1, 2, 3], [4, 1, 2]], [[3, 4, 1], [2, 3, 4], [1, 2, 3]]]
        ], dtype=int)
        # Se la configurazione salvata contiene il conf, aspettarsi 1
        self.assertEqual(Equivalent(conf, saved), 0)

#if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()