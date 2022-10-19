print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
n=int(input("Enter the number"));
a=0;
b=1;
sum=0;
count=1;
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a=b
  b=sum
  sum=a + b
