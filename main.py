from lesson import *
from time import *

def find_last_non_conflict(lesson_list, lesson_index):
    low, high = 0, lesson_index - 1
    while low <= high:
        mid = int((low + high) / 2)
        if lesson_list[mid].formatted_end_time <= lesson_list[lesson_index].formatted_start_time:
            if lesson_list[mid + 1].formatted_end_time <= lesson_list[lesson_index].formatted_start_time:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1


print("Enter Lessons Information In Structure Below:")
print("Structure:", "Name,", "Unit Number,", "Day In Week,", "Start Time,", "End Time.")
print("For Finish Enter Information Process Press Enter")

lessons = []
while True:
    information = input().split()
    if len(information) < 1:
        break
    lessons.append(lesson(information[0], information[1], information[2], time(information[3]), time(information[4])))

lessons = sorted(lessons, key=lambda x: x.formatted_end_time)
dp = []
for i in range(len(lessons)):
    dp.append([0, []])
path = []
path.append(lessons[0].name)
dp[0] = [int(lessons[0].unit), path]
for i in range(1, len(lessons)):
    include_unit = int(lessons[i].unit)
    l = find_last_non_conflict(lessons, i)
    if l != -1:
        include_unit += int(dp[l][0])

    if include_unit > dp[i - 1][0]:
        if l != -1:
            path = dp[l][1].copy()
            path.append(lessons[i].name)
        else:
            path = [lessons[i].name]
        dp[i] = [int(include_unit), path]
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
max_unit = dp[len(dp) - 1][0]
print("Max Units Involved:", max_unit)
print("Lesson Involved Name:")
for item in dp[len(dp) - 1][1]:
    print(item, end=" ")
