def mul(*values) :
    tmp = 1
    for value in values :
        tmp *= value
    return tmp

print(mul(5,7,9,10))