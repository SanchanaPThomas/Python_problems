for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    final_price_a=a-c
    final_price_b=b-d
    if final_price_b>final_price_a:
        print('First')
    elif final_price_b<final_price_a:
        print('Second')
    else:
        print('Any')
