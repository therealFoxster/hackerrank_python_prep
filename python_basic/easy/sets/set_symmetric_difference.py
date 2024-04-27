# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = set(input().split())
b = int(input())
y = set(input().split())

print(len(x.symmetric_difference(y)))