if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    score_set = set(arr)
    score_arr = [int(x) for x in score_set]
    score_arr.sort(reverse=True)
    print(score_arr[1])
