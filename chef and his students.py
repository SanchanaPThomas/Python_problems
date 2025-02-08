for i in range(int(input())):
    s=input()
    n=list(s)
    for i in range(len(n)):
        if n[i]=='<':
            n[i]='>'
        elif n[i]=='>':
            n[i]='<'
    m=0
    for i in range(len(n)-1):
        if n[i]=='>' and n[i+1]=='<':
            m=m+1
    print(m)
            
