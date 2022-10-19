print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
import numpy as np
num=np.arange(2,32,2)
print("First 15 even numbers")
print(num)

s=slice(2,8)
print("Elements from index 2 t0 8")
print (num[s])

index=num[-3:]
print("Last 3 elements of the array using negative index")
print(index)

alternate=num[::2]
print("Alternative elements of the array")
print(alternate)

lalternate=num[15:9:-2]
print("Last three alternate numbers")
print(lalternate)
