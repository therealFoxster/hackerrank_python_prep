n = int(input())
s = set(map(int, input().split()))

num_cmd = int(input())

for i in range(num_cmd):
    cmd, *args = input().split()
    if cmd == "pop":
        s.pop()
    elif cmd == "remove":
        s.remove(int(args[0]))
    elif cmd == "discard":
        s.discard(int(args[0]))
        
print(sum(s))