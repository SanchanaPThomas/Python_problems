for _ in range(int(input())):
    n=int(input())
    berth_map={
        1:(4,'LB'),
        4:(1,'LB'),
        2:(5,'MB'),
        5:(2,'MB'),
        3:(6,'UB'),
        6:(3,'UB'),
        7:(8,"SU"),
        8:(7,'SL'),
        }
    p=n%8
    if p==0:
        p=8
    partner_position, berth_type = berth_map[p]
    m=n//8
    if p==8:
        print(str((8*(m-1))+partner_position) + berth_type)
    else:
        print(str((8*m)+partner_position) + berth_type)
