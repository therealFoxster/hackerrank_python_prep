def check(s, f):
    for c in s:
        if f(c):
            print("True")
            return
    print("False")
            

if __name__ == '__main__':
    s = input()
    
    for f in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        check(s, f)