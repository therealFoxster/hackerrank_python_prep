# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

S, k = input().split()
S = list(S)
S.sort()
S = "".join(S)
k = int(k)

for i in range(1, k+1):
    for p in combinations(S, i):
        print("".join(p))