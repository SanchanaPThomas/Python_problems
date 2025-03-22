def solve():
    n, k = map(int, input().split())
    total_cost = 0
    for _ in range(n):
        t, d = map(int, input().split())
        if k > 0:
            if t <= k:
                k -= t
            else:
                total_cost += (t - k) * d
                k = 0
        else:
            total_cost += t * d
    print(total_cost)

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    solve()
