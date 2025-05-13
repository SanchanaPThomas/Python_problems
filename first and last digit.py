for _ in range(int(input())):
    n=int(input())
    last_digit=n%10
    
    n_str=str(n)
    first_digit=int(n_str[0])
    
    print(first_digit+last_digit)
