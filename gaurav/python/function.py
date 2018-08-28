'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list1,cmd,pos,val=None):
    if cmd=="remove":
        if pos=="beginning":
            return list1.pop(0)
        else:
            return list1.pop()
    else:
        if pos=="beginning":
            list1.insert(0,val)
            return list1
        else:
            return list1.append(val)
        
print(list_manipulation([1,2,3,4],"remove","beginning"))
print(list_manipulation([1,2,3,4],"add","beginning",20))