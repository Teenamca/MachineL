print("Name : Teena Tom")
print("Reg no : SJC21MCA-2043")
mob=int(input("Enter your 10 digit mobile number"));
list1=[];

for i in range(0,10):
    n=mob%10;
    list1.append(n);
    mob=mob//10;
print("numbers not in the list are")
for i in range(0,10):
     if i not in list1:
         print(i)


