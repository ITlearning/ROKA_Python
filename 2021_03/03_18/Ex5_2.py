sitting_min = 2
sitting_max = 10
people = 100
memo = {}

def problem(n_people, sitting) :
    key = str([n_people,sitting])
    
    if key in memo :
        return memo[key]
    if n_people < 0 :
        return 0
    if n_people == 0 :
        return 1
    count = 0
    for i in range(sitting, sitting_max + 1) :
        count += problem(n_people - i , i)
        
    memo[key] = count
    
    return count

print(problem(people, sitting_min))