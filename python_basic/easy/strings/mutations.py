def mutate_string(string, position, character):
    the_list = list(string)
    the_list[position] = character
    return "".join(the_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)