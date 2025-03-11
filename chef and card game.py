def digit_sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

for _ in range(int(input())):
    chef=0
    morty=0
    for i in range(int(input())):
        A,B=map(int,input().split())
        sum_a=digit_sum(A)
        sum_b=digit_sum(B)
        if sum_a>sum_b:
            chef+=1
        elif sum_a<sum_b:
            morty+=1
        else:
            chef+=1
            morty+=1
            
    if chef<morty:
        print(f"{1} {morty}")
    elif chef>morty:
        print(f"{0} {chef}")
    else:
        print(f"{2} {chef}")
