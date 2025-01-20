for i in range(int(input())):
    a,b,c,d,k=map(int,input().split())
    X = abs(c - a) + abs(d - b)
    if k >= X and (k - X) % 2 == 0:
        print("YES")
    else:
        print("NO")
