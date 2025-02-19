for i in range(int(input())):
    n=int(input())
    sum_n=sum(map(int,str(n)))
    x=n+1  

    while sum(map(int, str(x))) % 2 == sum_n % 2: 
        x+=1 

    print(x)
