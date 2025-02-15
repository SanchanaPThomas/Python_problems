def is_pseudo_sorted(array):
    inversion_count = 0
    
    
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            inversion_count += 1
            array[i], array[i + 1] = array[i + 1], array[i]
            if i > 0 and array[i-1] > array[i]:
                return "NO"
            if i + 2 < len(array) and array[i+1] > array[i+2]:
                return "NO"
        
        
        if inversion_count > 1:
            return "NO"
    
    return "YES"


for _ in range(int(input().strip())):
    n = int(input().strip())
    array = list(map(int, input().strip().split()))
    print(is_pseudo_sorted(array))
