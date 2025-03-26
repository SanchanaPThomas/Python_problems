import math
for _ in range(int(input())):
    n,a=map(int,input().split())
    x=int(math.sqrt(n))
    mega_square_side = x * a
    print(mega_square_side)
