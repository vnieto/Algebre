import numpy as numpy
t = numpy.genfromtxt('BIOGRID-ORGANISM-Rattus_norvegicus-3.2.120.tab2.txt',skip_header=1,usecols = (1, 2))
N = len(t) # importation of the 2, 3 columns from the BIOGRID file!
print "N =",N
a = zeros(N,N)

# Matrice adj
# commande: unique
