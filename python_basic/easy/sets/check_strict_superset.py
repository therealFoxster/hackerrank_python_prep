# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    s = set(map(int, input().split()))
    if len(s) >= len(A):
        print(False)
        exit()
    if not A.issuperset(s):
        print(False)
        exit()
print(True)