

# Last Semester's Gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Subjects
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

# Gradebook
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Extra 5 points for "visual arts"
gradebook[5][1] = 98

# Removing grade for poetry
gradebook[2].remove(gradebook[2][1])

# Adding "Passing" for poetry
gradebook[2].append("Pass")

# Combining both gradebooks
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)