def solve():
    prices = list(map(int, input().split()))
    text = input()
    
    present = set(text)
    cost = 0
    
    for i in range(26):
        char = chr(ord('a') + i)
        if char not in present:
            cost += prices[i]
            
    print(cost)

T = int(input())
for _ in range(T):
    solve()
            
