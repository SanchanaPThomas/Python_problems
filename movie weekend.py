for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    
    best_movie_index=0
    max_lr=-1
    max_r=-1
    
    for i in range(n):
        if l[i]*r[i]>max_lr:
            max_lr=l[i]*r[i]
            max_r=r[i]
            best_movie_index=i+1
        elif l[i]*r[i]==max_lr:
            if r[i]>max_r:
                max_r=r[i]
                best_movie_index=i+1
                
    print(best_movie_index)
