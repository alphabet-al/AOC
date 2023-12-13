from itertools import permutations

s = '???.###' 
condition = (1,1,3)

permute = list(permutations(s, len(s)))
print(permute)