"""
Q6. Student Grading System (2 marks)
Take marks from the user and print the grade.
Marks	Grade
90–100	A
80–89	B
70–79	C
60–69	D
Below 60	Fail

Extra condition: If marks are below 0 or above 100, print "Invalid Marks".
"""

marks = int(input("Enter the marks : "))

if marks >= 90 and marks < 100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
elif marks < 60:
    print("Fail")
else :
    print("Invalid Marks")