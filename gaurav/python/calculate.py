def calculate(make_float,operation,first,second,message=None):
    if operation=="add":
        result=first+second
    elif operation=="subtract":
        result=first-second
    elif operation=="multiply":
        result=first*second
    else:
        result=first/second
    if make_float==False:
        result=int(result)
    if message:
        return "{} {}".format(message,result)
    else:
        return "The result is{}".format(result)
    
print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"