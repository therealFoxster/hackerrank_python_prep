# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())
# a = map(int, (input().split()))
a = [int(x) for x in input().split()]

once = set()
many = set()

for e in a:
    if e not in many:
        if e in once:
            once.discard(e)
            many.add(e)
        else:
            once.add(e)

print(once.pop())

exit()

# Too slow
s = set(a)
for e in s:
    c = a.count(e)
    if c == 1:
        print(e)