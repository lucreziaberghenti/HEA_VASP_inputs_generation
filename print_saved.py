import numpy as np
import os

#read saved.npy, saved is an np array of dimensions: s, nslice, nrow, ncol
saved=np.load('saved.npy')
#read the number of saved configurations
s=saved.shape[0]

print("number of saved configurations: ",s) 
print("list of saved configurations:\n",saved,"\n")