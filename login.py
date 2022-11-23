from database import DataBase
from student import Student
from teacherAssistant import TeacherAssistent
from doctor import Doctor
from course import Course
from admin import Admin
import datetime

def studentMenu(loginStudent):
    menuNumber=int(input("1- view my course\n2-view new courses\n3-logout\nInter one of this menu numbers:\t"))
    while(menuNumber == 1):
        list_of_my_course = loginStudent.coursesStudentInfo()
        for i in list_of_my_course:
            print(i.info())
        if(len(list_of_my_course)==0):
            print("no registered courses")
            break
        operation = int(input("enter id course to view its assignmets with your solution and grades or enter (0) to back "))
        if(operation == 0):
            break
        else:
            Course(operation).viewSolutions(loginStudent.id)
            option = input("enter ## if you want to unrigester from cours other ways enter any thig")
            if(option != "##"):
                op = int(input("enter AssignmentID to add new solution on it or add 0 to back"))
                if(op == 0):
                    continue
                else:
                    solution = input("enter your solution : ")
                    loginStudent.add_solution_on_this_assignment(op,operation,solution)
                    pass
            else:
                op = int(input("enter course ID to unregister or add 0 to back"))
                if(op == 0):
                    continue
                else:
                    loginStudent.unrigester_from_course(op)
                break
    
    while(menuNumber == 2):
        
        for i in loginStudent.view_courses():
            print(f"cours ID : {i[0]}\tcourse Name : {i[1]}\tcourse password : {i[2]}")
        op = int(input("enter course ID if you want to register or enter (0) to back : "))
        if(op == 0):
                break
        else:
            password = input("enter courses password to continue : ")
            loginStudent.register_course(op,password)
        
        pass
    
    if(menuNumber == 3):    
        return False
    return True

def DoctorMenu(loginDoctor):
    menuNumber=int(input("1-show my messages. \n2-show recieve messages.\n3-send messages\n4- Create a new Course. \n5- view Courses. \n6- logout\nenter one of this numbers : "))
    if(menuNumber == 1):
        loginDoctor.viewMyMessage()
    elif(menuNumber == 2):
        loginDoctor.viewReceiveMessage()
    elif(menuNumber == 3):
        loginDoctor.sendmessage()
    if(menuNumber == 4):
        name = input("enter course name : ")
        password = input("enter course password : ")
        date_entry = input('Enter course dead_line in YYYY-MM-DD format')
        year, month, day = map(int, date_entry.split('-'))
        date1 = datetime.date(year, month, day)
        loginDoctor.createCourse(name,password,str(date1))
    
    while(menuNumber == 5):
        allCourses=loginDoctor.coursesList()
        for i in allCourses:
            print(Course(i).info())
        if(len(allCourses)==0):
            print("no registered courses")
            break
        option = input("1- Delete course \n2- view course Assignments\n3- send request for Teeacher Assistenent\n4-add post on course\n5- back\nenter one of this numbers : ")
        if(option == "5"):
            break
        op = int(input("enter course ID or add 0 to back : "))
        if(option == "1"):
                if(op == 0):
                    continue
                else:
                    loginDoctor.delete_course(op)
                    pass
        
        elif(option == "2"):
            if(op==0):
                break
            
            Course(op).courseWithAssignments()
            option = input("1- Delete Assignmets \n2- view solution on Assignments\n3- Add Assignment to course\n4- Add reqierment courses ID for this course\n5- back\nenter one of this numbers : ")
            
            if(option=="1"):
                loginDoctor.delete_Assignment(op)
            
            elif(option == "2"):
                Course(op).DoctorGradeReport()
                option = input("1- set grade and comment on solution\n2- back\nenter : ")
                if(option == "1"):
                    loginDoctor.setGrade(op)
                else:
                    break
            
            elif(option == "3"):
                Course(op).addAssignmet()
            
            elif(option == "4"):
                Course(op).set_requierment()
                
        elif(option == "3"):
            loginDoctor.sendRequestToTeacherAssistent()
        elif(option == "4"):
            loginDoctor.createpost()
        else:
            break

    if(menuNumber == 6):    
        return False
    return True

def TeacherAssistentMenu(loginTeacher):
    menuNumber=int(input("1-show my messages. \n2-show recieve messages.\n3-send messages\n4- show courses reqiests. \n5- view Courses. \n6- logout\nenter one of this numbers : "))
    if(menuNumber == 1):
        loginTeacher.viewMyMessage()
    
    elif(menuNumber == 2):
        loginTeacher.viewReceiveMessage()
    
    elif(menuNumber == 3):
        loginTeacher.sendmessage()
    
    elif(menuNumber == 4):
        loginTeacher.TA_Answer_requests()
    
    while(menuNumber == 5):
        allCourses=loginTeacher.coursesList()
        for i in allCourses:
            print(Course(i).info())
        if(len(allCourses)==0):
            print("no registered courses")
            break
        
        option = input("1- view course Assignments\n2-add post on course\n3- back\nenter one of this numbers : ")
        op = int(input("enter course ID to view its menu or add 0 to back : "))
        if(option == "1"):
            if(op==0):
                break 
            Course(op).courseWithAssignments()
            option = input("1- Delete Assignmets \n2- view solution on Assignments\n3- Add Assignment to course\n4- Add reqierment courses ID for this course\n5- back\nenter one of this numbers : ")
            
            if(option=="1"):
                loginTeacher.delete_Assignment(op)
            
            elif(option == "2"):
                Course(op).DoctorGradeReport()
                option = input("1- set grade and comment on solution\n2- back ")
                if(option == "1"):
                    loginTeacher.setGrade(op)
                else:
                    break
            
            elif(option == "3"):
                Course(op).addAssignmet()
            
            elif(option == "4"):
                Course(op).set_requierment()
            
            else:
                break
        
        elif(option == "2"):
            loginTeacher.createpost()
        
        else:
            break
    
    else:
        return False
    
    return True

def Login():
    user_name = input("enter user name:   ")
    if(user_name == "enter to admin"):
        A = Admin()
        A.acceptUsers()
        return None
    password = input("enter password:   ")    
    try:
        login_database = DataBase()
        account_info =list(login_database.execute(f"SELECT id,email,fullName,userName,type,Accept_type from users WHERE userName = '{user_name}' AND password = '{password}'"))[0]
        login_database.end()
        if(account_info[5] != 0):
            if(account_info[4]== 1):
                loginStudent = (Student(account_info[0],account_info[1],account_info[2],account_info[3],account_info[4]))
                s=True
                while(s):    
                    s = studentMenu(loginStudent)
                
            elif(account_info[4]==2):
                loginTeacherA = (TeacherAssistent(account_info[0],account_info[1],account_info[2],account_info[3],account_info[4],account_info[5]))
                s=True
                while(s):    s=TeacherAssistentMenu(loginDoctor)
            elif(account_info[4]==3):
                loginDoctor =  (Doctor(account_info[0],account_info[1],account_info[2],account_info[3],account_info[4],account_info[5]))
                s=True
                while(s):    s=DoctorMenu(loginDoctor)

        else:
            print("your account is not accepted by admin yet please try again later: ")
        return None
    
    except:
        print("try Again pass or user name is incorrect!!!")

def Register():
    types = {"s":1,"dr":3,"ta":2}
    user_name = input("Enter user name:   ")
    email = input("Enter your real email:   ")
    fullname = input("Enter your full name:   ")
    password = input("Enter password:   ")
    res = None
    if("@" not in email):
        print("this is a fake email!!!!  1")
        return False
    
    try:
        accept_type = 1
        emailType = types[input("Enter S if you are student | DR if you are a doctor | TA if you are Teacher Assistent:   ").lower()]
        if(emailType == 2):
            accept_type = 0
        elif(emailType == 3):
            accept_type = 0
        register_db=DataBase()
        register_db.execute(f"INSERT INTO users (email,fullName,userName,password,type,Accept_type)VALUES('{email}','{fullname}','{user_name}','{password}',{emailType},{accept_type});")
        register_db.end()
    
    except:
        print("Error in your information !!    ")


