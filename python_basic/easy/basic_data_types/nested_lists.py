if __name__ == '__main__':
    arr = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
    
    # Find second lowest score
    # Flatten arr
    flat_arr = []
    for sub_arr in arr:
        for el in sub_arr:
            flat_arr.append(el)
    # Grab floats from flattened arr
    scores = [el for el in flat_arr if type(el) is float]
    # Remove duplicates
    scores = list(set(scores))
    # Sort
    scores.sort()
    
    # Grab second student(s) with second lowest score
    results = [el for el in arr if el[1] == scores[1]]
    # Sort name in alphabetical order
    results.sort(key=lambda x: x[0])
    for el in results:
        print(el[0])
