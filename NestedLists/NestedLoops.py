def get_second_lowest_score(sorted_records):
    idx = 0
    for _ in sorted_records:
        if idx > 0:
            if sorted_records[idx - 1][1] != sorted_records[idx][1]:
                return sorted_records[idx][1]
        idx += 1
    return 0


studentRecords = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    studentRecords.append([name, score])

sorted_records = sorted(studentRecords, key=lambda l: l[1], reverse=False)
second_lowest_score = get_second_lowest_score(sorted_records)

for x in reversed(sorted_records):
    if x[1] == second_lowest_score:
        print(x[0])
