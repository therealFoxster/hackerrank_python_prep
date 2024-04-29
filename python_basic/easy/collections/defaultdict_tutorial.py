# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = [int(x) for x in input().split()]

A = defaultdict(list)
for i in range(1, n+1):
    w = input()
    A[w].append(i)

for i in range(m):
    w = input()
    arr = A[w]
    if len(arr) > 0:
        s = " ".join(map(str, arr))
        print(s)
    else:
        print("-1")