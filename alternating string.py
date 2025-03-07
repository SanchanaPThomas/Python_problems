for _ in range(int(input())):
    n=int(input())
    s=input()
    zeros=s.count('0')
    ones=s.count('1')
    if zeros<ones:
        print((2*zeros)+1)
    elif ones<zeros:
        print((2*ones)+1)
    else:
        print(2*zeros)
