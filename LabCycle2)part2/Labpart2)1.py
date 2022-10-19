print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
import numpy as np
from numpy.linalg import inv
print("Square matrix is :")
array = np.random.randint(10, size=(3, 3))
ainv=inv(array)
print(array)
print("Inverse of the matrix is :")
inverse=np.linalg.inv(array)
print(inverse)

print("The rank of matrix")
rank=np.linalg.matrix_rank(array)
print(rank)

print("Determinant of the matrix")
det = np.linalg.det(array)
print(int(det))

print("Transform matrix into 1D array :")
flat_array = np.ravel(array)
print('Flattened 1D Numpy array:')
print(flat_array)

w, v = np.linalg.eig(array)
print("Printing the Eigen values of the given square array:\n",w)
print("Printing Right eigenvectors of the given square array:\n",v)