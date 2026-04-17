n = int(input())
student_marks = {}

# --- This part is usually provided by the code stub ---
for _ in range(n):
    # Splits the line: the first word goes to 'name', the rest goes to a list called 'line'
    name, *line = input().split()
    # Converts the string scores into floating-point numbers
    scores = list(map(float, line))
    # Adds the name and scores to the dictionary
    student_marks[name] = scores

query_name = input()
# -------------------------------------------------------

# 1. Retrieve the list of marks for the queried student
query_scores = student_marks[query_name]

# 2. Calculate the average
# sum() adds all numbers in the list, len() counts how many numbers are in the list
average = sum(query_scores) / len(query_scores)

# 3. Print the result formatted to 2 decimal places
# The :.2f inside the f-string tells Python to format the float to 2 decimal places
print(f"{average:.2f}")