import re

def split_at_uppercase(s):
    pattern = r"(?=[A-Z])"  
    words = re.split(pattern, s)
    return [word for word in words if word] 
user_input = input("Enter a string: ")

split_result = split_at_uppercase(user_input)
print("Split words:", split_result)
