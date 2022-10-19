print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
def coprime(a,b):
    hcf=1;
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            hcf=i;
    return hcf==1;
first=int(input("Enter the first number"));
second=int(input("Enter the second number"));
if coprime(first,second):
    print('%d and %d are CO-PRIME' % (first, second))
else:
    print('%d and %d are not CO-PRIME' % (first, second))

