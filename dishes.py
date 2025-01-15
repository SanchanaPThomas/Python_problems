def dishes(N,A,B,C):
    max_dishes=min(B,A+C)
    if max_dishes>=N:
        return 'YES'
    else:
        return 'NO'
    
for i in range(int(input())):
     N, A, B, C = map(int, input().split())
     print(dishes(N, A, B, C))
