def print_rangoli(size):
    # your code goes here
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    num_lines = 1 + (size - 1) * 2
    for i in range(num_lines):
        x = size - 1 - i if i < size else i - size + 1
        c = [alpha[x]]
        for j in range(x + 1, size):
            c.insert(len(c), alpha[j])
            c.insert(0, alpha[j])
        c = "-".join(c)

        print(c.center(num_lines * 2 - 1, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)