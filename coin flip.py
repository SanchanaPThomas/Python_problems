for _ in range(int(input())):
    for _ in range(int(input())):
        i,n,q=map(int,input().split())
        if i==1:
            if q==2:
                print((n+1)//2)
            else:
                print(n//2)
            
        else:
            if q==1:
                print((n+1)//2)
            else:
                print(n//2)
