import matplotlib.pyplot as plt

# Act 1 - 6 Scores
act_scores = [100, 95, 95, 100, 95, 100]

# Quiz 1 Score
# Find it in the rate of 100s
quiz_score = (20/20)*100

# Exam Score
exam_score = 94

# Written Score
written_average = (sum(act_scores + [quiz_score]) / 7)
written_score = (written_average) * 0.6

# Midterm Exam Score
midterm_exam_score = exam_score * 0.4

# Total Score
total_score = written_score + midterm_exam_score

# Print the Total Score
print ("Written Grade: ", written_score)
print ("Exam Grade: ", midterm_exam_score)
print("Total Computer Grade: ", total_score)

# Create a list of the different grades
grades = [written_average, exam_score, total_score]

# Create a bar chart of the grades
plt.bar(["Written Grade", "Exam Grade", "Total Grade"], grades)

# Set the chart title and labels
plt.title("Midterm Exam Grades")
plt.xlabel("Grade")
plt.ylabel("Score")

# Show the chart
plt.show()