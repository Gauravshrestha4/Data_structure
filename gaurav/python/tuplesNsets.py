#initialise a tuple
t=("math","science","history","english","computers") #immutable

#count(element)
print(t.count("math"))

#index(elemnt) index of first occurence
print(t.index("science"))

#initiialise a set 
x={3,4,2,55,32,1,3} #will only consider unique values
print(x)

#add and item in a set
x.add(44) #returns nothing
x.add(4) #already present but no error is thrown 
print(f"after adding items {x}")

#remove an item from the set
x.remove(44)  #return nothing
# x.remove(33)  #will throw an error
x.discard(33) #no error is thrown 
print(f"after adding items {x}")

#copy set
another_x=x.copy()
print(another_x==x) #true
print(another_x is x) #false

#clear set
another_x.clear()

y={45,2,3,4,1,9}
#union
print(x|y)

#intersection
print(x & y)