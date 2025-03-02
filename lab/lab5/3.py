import re

def find_sequences(s):
    pattern = r"\b[a-z]+_[a-z]+\b"  
    matches = re.findall(pattern, s)
    return matches


user_input = input("Enter a string: ")


sequences = find_sequences(user_input)
if sequences:
    print("Matching sequences:", sequences)
else:
    print("No matching sequences found.")
