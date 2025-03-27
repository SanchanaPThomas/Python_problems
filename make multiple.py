def solve():
    a, b = map(int, input().split())
    if a == b:
        print("YES")
    else:
        diff = b - a
        if a <= diff:
            print("YES")
        else:
            print("NO")

t = int(input())
for _ in range(t):
    solve()
