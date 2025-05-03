for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    k=x-y
    print(w+(k*z))
