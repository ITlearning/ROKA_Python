key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(0,4,1) :
    character[key_list[i]] = value_list[i]
    
print(character)