def average(array):
    # your code goes here
    the_set = set(array)
    return sum(the_set) / len(the_set)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)