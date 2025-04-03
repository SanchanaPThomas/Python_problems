for _ in range(int(input())):
    n,p=map(int,input().split())
    i=list(map(int,input().split()))
    hard=0
    cakewalk=0
    for j in i:
        if j<=(p//10):
            hard+=1
        elif j>=(p//2):
            cakewalk+=1
    if hard==2 and cakewalk==1:
        print('yes')
    else:
        print('no')
