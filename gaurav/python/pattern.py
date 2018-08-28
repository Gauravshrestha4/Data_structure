n=int(input("enter a number "))
i=0

while i<n:
    if i<n/2:
        j=1
        while j<=n:
            print(f"{2*n*i +j} ",end='', flush=True)
            j+=1
        print("\n")
    
    else:
        j=1
        while j<=n:
            print(f"{n*(2*(n-i)-1)+j} " ,end='',flush=True)
            j+=1
        print("\n")
    i+=1