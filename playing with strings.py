for _ in range(int(input())):
    n=int(input())
    r=input()
    s=input()
    z=('0','1')
    for i in z:
         if s.count(i)!=r.count(i):
             print('NO')
             break
    else:
        print('YES')
