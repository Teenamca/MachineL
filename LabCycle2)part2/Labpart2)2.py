import numpy as np
rows = int(input("Enter the Number of rows :"))
column = int(input("Enter the Number of Columns:"))
print("Enter the elements of First Matrix:")
a = [[int(input()) for i in range(column)] for i in range(rows)]
print("First Matrix is:")
for n in a:
  print(n)

print("\nPower of the matrix :")
power=np.power(a, 3)
print(power)

print("\nuse multiply find power :")
square=np.multiply(a,a)
cube=np.multiply(square,a)
print(cube)

print("\nIdentity of the matrix is :")
id=np.identity(2,dtype=float)
print(id)

print("Power of each element of matrix is : ")
arrD = np.power(a,3)
print(arrD)

print("Element wise power os the matrix is :")
arrE=np.power(a,2)
print(arrE)