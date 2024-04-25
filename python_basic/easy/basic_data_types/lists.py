if __name__ == '__main__':
    N = int(input())
    
    the_list = []
    
    for _ in range(N):
        line = input().split(" ")
        cmd = line[0]
        if cmd == "print":
            print(the_list)
        elif cmd == "sort":
            the_list.sort()
        elif cmd == "pop":
            the_list.pop(len(the_list) - 1)
        elif cmd == "reverse":
            the_list.reverse()
        else:
            val1 = int(line[1])
            if cmd == "insert":
                val2 = int(line[2])
                the_list.insert(val1, val2)
            elif cmd == "remove":
                the_list.remove(val1)
            elif cmd == "append":
                the_list.append(val1)

    exit()

    # ChatGPT's solution
    for _ in range(N):
        line = input().split()
        cmd, *args = line  # Unpack command and optional arguments
        
        commands = {
            "print": lambda: print(the_list),
            "sort": lambda: the_list.sort(),
            "pop": lambda: the_list.pop(),
            "reverse": lambda: the_list.reverse(),
            "insert": lambda: the_list.insert(int(args[0]), int(args[1])),
            "remove": lambda: the_list.remove(int(args[0])),
            "append": lambda: the_list.append(int(args[0]))
        }
        
        commands[cmd]()  # Execute the corresponding command function
