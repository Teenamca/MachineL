print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
import numpy as np
A=np.array([[2,1,-2],
            [3,0,1],
            [1,1,-1]])
B=np.array([[-3],
              [5],
              [-2]])
print("\nThe inverse of the matrix A is:")
inv=np.linalg.inv(A)
print(inv)
print("\nX=A inverse B=")
AB=np.linalg.solve(inv, B)
print(AB)
