n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
average_score = 0.00
for x in student_marks[query_name]:
    average_score += x

print("{0:.2f}".format(average_score/(len(student_marks[query_name]))))
