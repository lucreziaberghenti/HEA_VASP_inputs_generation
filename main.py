import math
import numpy as np
import os
import functions as fn

# dimensions of unit cell (x,y,z)=(5,4,3)
ncol, nrow, nslice= 5, 4, 3

#define the elements of the new configuration
#np.arange produces the np array [1,2,3,4,5]
#np.repeat repeates each element 5 times (HEA have equal concentration of each element)
#60 atoms in total
n=np.repeat(np.arange(1,6), 5)

#path of the input settings
settings_path='./tests/settings_tests.json'

# create an np array of dim (60, 3) of cartesian coordinates (x,y,z) for each atom
# positions of lattice sites don't depend on configuration but only on lattice geometry
coord=fn.Coordinates(settings_path)

# convert the np coord array into a list in order to use python ase function
positions=coord.tolist()

# saved will be an array of (3,4,5)-dim representing a configuration each
saved=np.array([],dtype=int)

# check if 'saved.npy' exists
# define the path where saved should be searched
path = './saved.npy'

if os.path.exists(path):
    # saved is an np array of dimensions: s, nslice, nrow, ncol
    saved=np.load('saved.npy')
    # read the number of saved configurations
    s=saved.shape[0]
    
else:
    #number of saved configurations is zero
    s=0

# generate inequivalent random configuration
# generate random matrix (nslice x nrow x ncol)=(3, 4, 5) having elements 1,2,3,4,5 repeated 12 times each
# the function newConf also check that in "saved" there is not an equivalent conf to the one generated
conf=fn.newConf(saved, nslice, nrow, ncol, n)

# increment the counter since a new configuration is added
s+=1

# save the new configuration
saved=np.append(saved, conf)

# create array of strings where atomic species are listed in order to use python ase
species=fn.Generate_species(conf)

# function that generates VASP input files
fn.VASP_input(species,positions,s,settings_path)

# reshape using the update number of saved configurations s: (s,nslice,nrow,ncol) 
# since when I add the new configuration "saved" loses its original shape
saved=np.reshape(saved, (s,nslice,nrow,ncol))
np.save('saved.npy',saved)