import unittest
import numpy as np
from functions import newConf

class Test_newConf(unittest.TestCase):

    def test_generate_new_conf_dimensions(self):
        # Test per controllare la dimensione della configurazione generata
        saved = []
        conf = newConf(saved)
        self.assertEqual(conf.shape, (3, 4, 5), "La dimensione della configurazione generata è errata")
    
    def test_generate_new_conf_distribution(self):
        # Test per controllare la distribuzione degli elementi nella configurazione
        saved = []
        conf = newConf(saved)
        
        n_expected = np.array([12, 12, 12, 12, 12])
        n_generated = np.array([np.sum(conf == i) for i in range(1, 6)])
        
        self.assertTrue(np.array_equal(n_generated, n_expected), 
                        "La distribuzione degli elementi nella configurazione generata è errata")

    def test_generate_non_equivalent_conf(self):
        # Test per verificare che la nuova configurazione non sia equivalente a quelle già salvate
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
        
        # Verifica che la nuova configurazione non sia equivalente a quella salvata
        self.assertFalse(Equivalent(conf, saved), 
                         "La nuova configurazione generata è equivalente a una già salvata")

    def test_generate_unique_conf(self):
        # Test per verificare che più chiamate a newConf generino configurazioni uniche
        saved = []
        conf1 = newConf(saved)
        saved.append(conf1)
        conf2 = newConf(saved)
        
        self.assertFalse(np.array_equal(conf1, conf2), 
                         "La seconda configurazione generata è uguale alla prima, dovrebbe essere diversa")

if _name_ == '_main_':
    unittest.main()