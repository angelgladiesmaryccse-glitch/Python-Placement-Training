n=int(input())
n=2*n-1
for r in range(1,n+1):
    for c in range(1,n+1):
        if(r==c or r+c==n+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
