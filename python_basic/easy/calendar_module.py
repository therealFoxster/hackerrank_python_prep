import calendar

in_str = input()
arr = in_str.split(" ")
arr = [int(x) for x in arr]

weekday = calendar.weekday(arr[2], arr[0], arr[1])
day_name = calendar.day_name[weekday]
print(day_name.upper())