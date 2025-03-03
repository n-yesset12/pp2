def all_true(tup):
    return all(tup) 

user_input = input()
tup = tuple(map(int, user_input.split()))  

result = all_true(tup)
print("All elements are True:", result)
