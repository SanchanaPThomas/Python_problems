for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    a_sort=sorted(a)
    for i in range(n):
        if a[k-1]==a_sort[i]:
            print(i+1)
            break
