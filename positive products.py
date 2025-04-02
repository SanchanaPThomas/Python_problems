def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    pos_count = 0
    neg_count = 0
    
    for x in a:
        if x > 0:
            pos_count += 1
        elif x < 0:
            neg_count += 1
            
    result = (pos_count * (pos_count - 1) // 2) + (neg_count * (neg_count - 1) // 2)
    print(result)

#handle multiple test cases
t = int(input())
for _ in range(t):
    solve()
