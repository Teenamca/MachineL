print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
str = input("Enter a string: ")
count = {x:sum([1 for char in str if char == x]) for x in 'aeiou'}
print(count)



