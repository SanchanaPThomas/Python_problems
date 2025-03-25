def solve():
    n = int(input())
    a = list(map(int, input().split()))

    xor_all = 0
    for x in a:
        xor_all ^= x

    min_xor = xor_all  
    for x in a:
        min_xor = min(min_xor, xor_all ^ x)

    print(min_xor)



t = int(input())
for _ in range(t):
    solve()
