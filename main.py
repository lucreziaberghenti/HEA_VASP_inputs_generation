import math
import numpy as np
import os
import functions

#global variables
a_fcc=3.6 #lattice parameter, angstrom 
a_nn=a_fcc/math.sqrt(2) #distance between nn in xy-plane, side of equilateral triangle

ncol, nrow, nslice= 5, 4, 3
#np arrays that contains the number of atoms for each element labeled by 1,2,3,4,5: n=[n1,n2,n3,n4,n5]
n=np.array([12, 12, 12, 12, 12],dtype=int)
n_tot=np.sum(n)

#create an np array of dim (60, 3) of cartesian coordinates (x,y,z) for each atom
#positions of lattice sites don't depend on configuration
coord=np.zeros([n_tot,3],dtype=float) 
coord=functions.Coordinates()

#convert the np coord array into a list in order to use python ase function
positions=coord.tolist()

#saved will be an array of (3,4,5)-dim arrays representing a configuration each
saved=np.array([],dtype=int)

#check if 'saved.npy' exists
#define the path where saved should be searched
path = './saved.npy'

if os.path.exists(path):
    #saved is an np array of dimensions: s, nslice, nrow, ncol
    saved=np.load('saved.npy')
    #read the number of saved configurations
    s=saved.shape[0]
    
else:
    #number of saved configurations is zero
    s=0
    
print("number of saved configurations: ",s)   
#print("list of saved configurations:\n",saved,"\n")


#generate inequivalent random configuration
#generate random matrix (nslice x nrow x ncol)=(3, 4, 5) with elements 1,2,3,4,5 repeated n1,n2,n3,n4,n5 times
#the function newConf also check that in "saved" there is not an equivalent conf to the one generated
conf=functions.newConf(saved)

#increment the counter
s+=1

print("conf n. ", s, " generated:\n",conf,"\n")
saved=np.append(saved, conf)

#create array of strings where atomic species are listed in order to use python ase
species=functions.Generate_species(conf)

#function that generates VASP input files
functions.VASP_input(species,positions,s)

#reshape using the update number of saved configurations s, also because when I add the new conf "saved" becomes linear
saved=np.reshape(saved, (s,nslice,nrow,ncol))
np.save('saved.npy',saved)
print("updated list of saved configurations:\n", saved)