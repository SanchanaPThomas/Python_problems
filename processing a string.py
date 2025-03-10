for _ in range(int(input())):
    s=input()
    m=0
    for i in s:
        if 96<ord(i)<123:
            continue
        else:
            k=int(i)
            m+=k
    print(m)
