from itertools import permutations

def print_permutations(s):
    perm_list = [''.join(p) for p in permutations(s)]
    for perm in perm_list:
        print(perm)

print_permutations(input())
