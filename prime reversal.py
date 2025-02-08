for i in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    a_ones=a.count('1')
    b_ones=b.count('1')
    if a_ones==b_ones:
        print('yes')
    else:
        print('no')
