student = {"name": "marco",
           "roll_number": "33",
           "register_number": "MCA0033",
           "department": "Computer Science",
           "semester": 3}

student["total_mark"] = 95  
marks = student["total_mark"]
if marks >= 90:
    grade = "A"
elif marks >= 82:
    grade = "B"
elif marks >= 75:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "P"
else:
    grade = "F"
    
student["grade"] = grade
student.pop("roll_number")
print(student)



