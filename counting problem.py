for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    total_sum = sum(a)
    
    if total_sum % 2 == 1:
        print("NO")
    else:
        # Check for at least one odd number
        has_odd = any(x % 2 == 1 for x in a)
        if has_odd:
            print("YES")
        else:
            print("NO")
