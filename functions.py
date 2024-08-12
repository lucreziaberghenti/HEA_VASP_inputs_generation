import math
import numpy as np
import os
from ase.calculators.vasp import Vasp #ase is a tool used just to create input files that (not here) I run on VASP (Vienna Ab initio Simulation Package)

#global variables
a_fcc=3.6 #lattice parameter, angstrom 
a_nn=a_fcc/math.sqrt(2) #distance between nn in xy-plane, side of equilateral triangle

ncol, nrow, nslice= 5, 4, 3
#np arrays that contains the number of atoms for each element labeled by 1,2,3,4,5: n=[n1,n2,n3,n4,n5]
n=np.array([12, 12, 12, 12, 12],dtype=int)
n_tot=np.sum(n)


#function that creates all the VASP input files using ase.calculators.vasp
#it takes as input: the chemical species of atoms, their positions and the number of the configuration generated
#it returns the input files
def VASP_input(species, positions, n):

#for simplicity when new conf is generated we use numbers, then the following function translates from numbers to elements
def element(x): 

#function that outputs a (60,3) np.array writing the lattice sites for each atom in cartesian coordinates [x, y, z] of a (111)-fcc lattice
def Coordinates(): 

#function that checks if m2 is present in m1 (m2 has dimensions < than m1) and returns 1 if matrix is present otherwise returns 0 if not
#in our case m1 = 4x(random conf) and m2=saved matrix
def Find(m1,m2): 

#function that takes as input a conf of dim (nslice,nrow,ncol) and returns a matrix 8-times bigger
def Big_conf(conf):

#functions that checks if the input matrix is equivalent to the matrix saved in "saved.npy"
def Equivalent(conf):

#function that generates a new random configuration non equivalent to the ones saved
def newConf(saved):