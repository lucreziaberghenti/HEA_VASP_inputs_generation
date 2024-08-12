import numpy as np
import os

#reset all saved configurations
#delete saved.npy
path = './saved.npy'
if os.path.exists(path):
 os.remove(path)

#delete input files for each configuration
path='./'
for fname in os.listdir(path):
    if fname.startswith("conf_"):
        os.remove(os.path.join(path, fname))