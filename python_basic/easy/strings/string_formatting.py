def print_formatted(number):
    arr = []
    for d in range(1, number + 1):
        o = oct(d)[2:] # w/o "0o"
        h = hex(d)[2:] # w/o "0x"
        b = bin(d)[2:] # w/o "0b"
        arr.append([d, o, h, b])
    
    max_len = len(bin(number)[2:])
    
    for e in arr:
        print(
            str(e[0]).upper().rjust(max_len) +
            str(e[1]).upper().rjust(max_len + 1) +
            str(e[2]).upper().rjust(max_len + 1) +
            str(e[3]).upper().rjust(max_len + 1)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)