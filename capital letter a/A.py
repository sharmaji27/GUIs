while(1):
    print("ENTER THE VALUE OF N GREATER THAN 2")
    n=int(input())
    r=n//3
    for row in range(0,n):
        if (row in range(0,r)) or (row in range(n//2,(n//2)+r)) :
            for i in range(0,n):
                print("*\t",end='')

        else:
            for col in range (0,n):
                if col in range(0,r) or col in range (n-r,n):
                    print("*\t", end='')
                else:
                    print(" \t", end='')

        print("\n\n")