def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        # if string[i] == sub_string[0] and string[i + 1] == sub_string[1] and string[i + 2] == sub_string[2]: # Only works for substring length 3
        if string[i:i+ len(sub_string)] == sub_string:
            count += 1
    return count

    # ChatGPT
    return string.count(sub_string) # 💀

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)