def is_prime(n):
    for j in range(2,n):
        if n%j==0:
            return False
    return True
for _ in range(int(input())):
    x,y=map(int,input().split())
    i=1
    while True:
        if is_prime(x+y+i):
            print(i)
            break
        i+=1
