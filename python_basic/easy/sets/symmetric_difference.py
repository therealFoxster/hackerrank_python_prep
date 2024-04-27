# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

diff = a.difference(b).union(b.difference(a))

arr = list(diff)
arr.sort()

for n in arr:
    print(n)
