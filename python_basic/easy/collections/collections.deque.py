# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()
N = int(input())

for _ in range(N):
    cmd, *arg = input().split()
    if cmd == "append":
        d.append(arg[0])
    elif cmd == "pop":
        d.pop()
    elif cmd == "popleft":
        d.popleft()
    elif cmd == "appendleft":
        d.appendleft(arg[0])
        
print(" ".join(map(str, d)))