# Prompt the user to enter three test scores
score1 = input("Enter the first test score: ")
score2 = input("Enter the second test score: ")
score3 = input("Enter the third test score: ")
S1 = float(score1)
S2 = float(score2)
S3 = float(score3)
# Calculate the average of the test scores
average = ((S1+S2+S3) / 3)
# Display each test score and the average
print("Test Score 1:", score1)
print("Test Score 2:", score2)
print("Test Score 3:", score3)
print("Average Score:", average)