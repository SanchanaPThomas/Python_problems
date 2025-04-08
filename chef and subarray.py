n=int(input())
a=list(map(int,input().split()))

max_len=0
current_len=0

for x in a:
    if x==0:
        max_len=max(max_len,current_len)
        current_len=0
    else:
        current_len+=1
        
max_len=max(max_len,current_len) 
print(max_len)
