print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
import numpy as np

arr=np.array([2,4,6,8,10])
print("Original list :", arr)
print("\n1D array using append :")
newarr=np.append(arr, 21)
print(newarr)

TwoD=np.array([[2,1,3],[1,3,4]])
print("\n2D List :")
print(TwoD)
print("\n2D array using append :")
newTwoD=np.append(TwoD, [25,22,20])
print(newTwoD)

TwoD1=np.array([[3,6,1],[2,9,8]])
result=np.append(TwoD,TwoD1, axis=1)
print("\nnew value :")
print(result)