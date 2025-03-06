def solve():
    n1, n2, n3 = map(int, input().split())
    
    all_voter_ids = []
    for _ in range(n1 + n2 + n3):
        voter_id = int(input())
        all_voter_ids.append(voter_id)
    
    
    counts = {}
    for voter_id in all_voter_ids:
        counts[voter_id] = counts.get(voter_id, 0) + 1
    
    final_list = [voter_id for voter_id, count in counts.items() if count >= 2]
    
    
    final_list.sort()
    
    print(len(final_list))
    for voter_id in final_list:
        print(voter_id)

solve()
