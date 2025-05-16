student = {'rohan':'59','Sam':'98','alice':'85','Alice':'78'}
u_name = input("Enter the student's name: ")

if u_name in student:
    print(f"{u_name.capitalize()} marks : {student[u_name]}")