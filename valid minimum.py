for _ in range(int(input())):
    a,b,c=map(int,input().split())
    nums = sorted([a, b, c])
    if nums[0] == nums[1]:
        print("YES")
    else:
        print("NO")
