print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
def bubble_sort(list1):

    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1


list1 = [3,7,8,5,1]

print("The unsorted list is: ", list1)
print("The sorted list is: ", bubble_sort(list1))