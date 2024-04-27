# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range(T):
    num_A = int(input())
    A = set(input().split())
    num_B = int(input())
    B = set(input().split())
    print(A.issubset(B))