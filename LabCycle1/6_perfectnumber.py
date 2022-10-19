print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
n=int(input("Enter number "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("Number is perfect")
else:
    print("Number is not perfect")

