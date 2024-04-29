# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, k = input().split()
S = list(S)
S.sort()
S = "".join(S)
k = int(k)

for p in permutations(S, k):
    print("".join(p))
