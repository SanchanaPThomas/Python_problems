for _ in range(int(input())):
    s=input()+'0'
    m=0
    for i in range(len(s)-1):
        if s[i]!='0' and s[i+1]=='0':
            m+=1
    print(m)
