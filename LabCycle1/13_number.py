print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
n = int(input("Enter a positive number : "))
n_str = str(n)
while (n > 0):
    n -= sum([int(i) for i in list(n_str)])
    n_str = list(str(n))
    print(n)