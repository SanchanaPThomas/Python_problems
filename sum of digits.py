for _ in range(int(input())):
    n=int(input())
    s=0
    while n>0:
        s+=(n%10)
        n=n//10
    print(s)
        
