# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
Student = namedtuple("Student", input())

students = []
for _ in range(N):
    row = input().split()
    students.append(Student(row[0], row[1], row[2], row[3]))
    
marks = [int(student.MARKS) for student in students]

print(sum(marks) / N)