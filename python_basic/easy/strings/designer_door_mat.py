# Enter your code here. Read input from STDIN. Print output to STDOUT

(N, M) = map(int, input().split(" "))

mid = N // 2
x = 0

for i in range(N):
    s = ""
    for _ in range(1 + x * 2):
        s += ".|."
    if (i == mid):
        s = "WELCOME"
    print(s.center(M, "-"))
    if i < mid:
        x += 1
    else:
        x -= 1