print("enter no of students")
student_list = []
num_students = int(input())

for i in range(num_students):

    name = input()
    score = float(input())

    student_list.append([name,score])

scores_only = []

for student in student_list:
    scores_only.append(student[1])
unique_scores_set = set(scores_only)

unique_scores_list = list(unique_scores_set)

unique_scores_list.sort()

second_lowest = unique_scores_list[1]




print("the second lowest score is :", second_lowest)