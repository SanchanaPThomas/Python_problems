for i in range(int(input())):
    A,B=map(int,input().split())
    limak=0
    bob=0
    turn=1
    while(1):
        if turn%2==1:
            limak+=turn
            if limak>A:
                print('Bob')
                break
        else:
            bob+=turn
            if bob>B:
                print('Limak')
                break
        turn+=1
            
