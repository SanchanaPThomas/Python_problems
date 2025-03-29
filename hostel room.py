for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    max_people=x
    for i in a:
        x+=i
        max_people=max(max_people,x)
    print(max_people)
