for _ in range(int(input())):
    n=int(input())
    i=list(map(int,input().split()))
    
    inside=set()
    max_people=0
    current_people=0
    
    for employee_id in i:
        if employee_id in inside:
            inside.remove(employee_id)
            current_people-=1
        else:
            inside.add(employee_id)
            current_people+=1
        max_people=max(max_people,current_people)
    print(max_people)
    
