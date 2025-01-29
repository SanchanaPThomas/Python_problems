for i in range(int(input())):
    n=int(input())
    s=list(input())
    for i in range(0,n-1,2):
        s[i],s[i+1]=s[i+1],s[i]
    for j in range(n):
        s[j]=chr(ord('a')+(ord('z')-ord(s[j])))
    print("".join(s))
    
