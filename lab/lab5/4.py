import re

def find_sequences(s):
    pattern = r"\b[A-Z][a-z]+\b"  
    matches = re.findall(pattern, s)
    return matches

user_input = input()

sequences = find_sequences(user_input)
if sequences:
    print("Matching sequences", sequences)
else:
    print("No matching sequences")
