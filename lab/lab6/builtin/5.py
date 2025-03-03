def all_true(tup):
    return all(tup) 

user_input = input("Enter tuple elements separated by spaces (e.g., 1 0 3): ")
tup = tuple(map(int, user_input.split()))  

result = all_true(tup)
print("All elements are True:", result)
