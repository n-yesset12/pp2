import re
 
def match_pattern(s):
    pattern = r'ab*'  
    if re.fullmatch(pattern, s):
        return True
    else:
        return False
 
test_strings = ['a', 'ab', 'abb', 'abbb', 'b', 'ba', 'aab', 'abc']
 
for string in test_strings:
    print(f"'{string}': {match_pattern(string)}")