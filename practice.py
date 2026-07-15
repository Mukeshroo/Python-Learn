#Three students appear for a scholarship examination.
#Write a Python program to identify the student with the highest marks.

student1 = int(input("enter your scholarship examination highest marks: "))
student2 = int(input("enter your scholarship examination highest marks: "))
student3 = int(input("enter your scholarship examination highest marks: "))

if(student1>student2 and student1>student3):
    print("student1 get the scholarship")

elif(student2>student1 and student2>student3):
    print("student2 get the scholarship")

else:
    print("student3 get the scholarship")