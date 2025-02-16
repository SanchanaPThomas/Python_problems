for i in range(int(input())):
    n=int(input())
    b=list(map(int,input().split()))
    count_1=b.count(1)
    if count_1%2==0:
        print('YES')
    else:
        print('NO')
