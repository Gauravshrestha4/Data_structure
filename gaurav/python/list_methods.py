names=[]
for x in range(3):
    names.append(input("enter the name "))

print(names)
names.sort()
print(f"names in sorted order {names}")
names.sort(reverse=True)
print(f"names in reversed sorted order {names}")

#clear a list
names.clear()
print(f"names after clear {names}")

names.extend(["shubham","shubham"])
print(f"names after extend {names}")

# insert(position,element)
pos=input("enter the position to insert new name:")
names.insert(int(pos),"sachin")
print(f"names after insertion {names}")

#remove(element) does not return anything
names.remove("sachin")
print(f"names after removing {names}")

#insert any number of items in a list
names.extend(["are","friends"])
print(" ".join(names))

#reverse a list
names.reverse()
print(f"names after reverse {names}")

#get count-count(element)
print(f"count:{names.count('gaurav')}")

#find an element-index(element,startpoint,endpoint)
print(names.index("shubham")) #returns the index ,error if not in list
print(names.index("shubham",1))
print(names.index("shubham",3,4))