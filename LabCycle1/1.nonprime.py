print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
lower=int(input("Enter a value for lower digit :"))
upper=int(input("Enter a value for upper digit : "))
print("The Non Prime Numbers are : ")
for i in range(lower,upper):
 for j in range(2,upper):
   if(i%j==0) and(j!=i):
    print(i)
    break
