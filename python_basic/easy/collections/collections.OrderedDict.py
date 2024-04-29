# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

N = int(input())

items = OrderedDict()
for _ in range(N):
    *name, price = input().split()
    name = " ".join(name)
    net_price = int(price) + items.get(name, 0)
    items[name] = net_price
    
for name, net_price in items.items():
    print(name, net_price)