def flatten(data) :
    tmp = []
    for i in data :
        if type(i) == list:
            tmp += flatten(i)
        else :
            tmp.append(i)
            
    return tmp
        
example = [[1,2,3], [4,[5,6]], 7, [8,9]]
print(flatten(example))