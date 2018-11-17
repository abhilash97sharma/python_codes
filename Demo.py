#lst = [(1,'a'),(2,'b'),(3,'c'),(4,'d')]
#lst1 = list[1,2,3,4,5]
lst1 = [3,5,1,2,3]
#print(lst[2])
lst2 = lst1.copy()    #for copying a list
lst1.sort(reverse=True)
lst2.sort()
print(lst1)
print(lst2)