def is_all_strings(item):
    # all([type(x)=='str' for x in item])
    for x in item:
    	print(type(x)==str)

is_all_strings(["gaurav","sachin","rishabh"])