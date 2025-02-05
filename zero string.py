for i in range(int(input())):
    n=int(input())
    s=input()
    count_0 = s.count('0')
    count_1 = s.count('1')
    
    min_operations = min(count_1, 1 + count_0)
    
    print(min_operations)
