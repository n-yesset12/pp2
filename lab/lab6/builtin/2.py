def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

user_input = input()

upper, lower = count_case(user_input)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
