for _ in range(int(input())):
    n, b, m = map(int, input().split())
    total_time = 0
    while n > 0:
        if n % 2 == 0:
            problems_done = n // 2
        else:
            problems_done = (n + 1) // 2
        
        session_time = problems_done * m
        total_time += session_time
        
        n -= problems_done
        
        if n > 0:
            total_time += b
        
        m *= 2
    print(total_time)
