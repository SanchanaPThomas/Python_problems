for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=[0]*11
    
    for i in a:
        count[i]+=1
    
    m=max(count)
    s=0
    z=0
    for i in range(len(count)):
        if count[i]==m:
            z=i
            s+=1
            if s>1:
                print('confused')
                break
    else:
        print(z)
            
