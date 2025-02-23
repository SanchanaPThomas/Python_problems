for _ in range(int(input())):
    n=int(input())
    max_scores=[0]*9
    for i in range(n):
        p,s=map(int,input().split())
        if p<9:
            max_scores[p-1]=max(max_scores[p-1],s)
            
    total_score=sum(max_scores)
    print(total_score)
            
