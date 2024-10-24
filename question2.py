# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F
 
 
 #ANSWER
def student_score ():
    student_mark = int(input("Enter student marks:"))
    if student_mark >= 90 and student_mark <=100:
     print("Grade A")
    elif student_mark >=80 and student_mark <=89:
        print("Grade B")
    elif student_mark >= 70 and student_mark <=79:
        print("Grade C")  
    elif student_mark >= 60 and student_mark <=69:
        print("Grade D ")
    elif student_mark >= 50 and student_mark <=59:
        print("Grade E")
    else:
        student_mark <= 40
        print("grade F") 
student_score()   
                   
     
     

    
 
 
 
 
 
 