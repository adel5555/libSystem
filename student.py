from person import Person
from database import DataBase
from course import Course
def convertToSqlTuple(l):
    s="("
    for i in l:
        s+=str(i)+","
    if(len(s)>1):
        s=s[:-1]+")"
    else:
        s = "()"
    return s
class Student(Person):
    
    def __init__(self, id, email, full_name, user_name, type_ID):
        super().__init__(id, email, full_name, user_name, type_ID)
        self.list_my_courses = []
    
    def studentCourses(self):
        studentDB = DataBase()
        self.list_my_courses = list(studentDB.execute(f"SELECT course_ID FROM enrolled_course WHERE user_id = {self.id} AND Account_type = 1"))
        self.list_my_courses = [course[0] for course in self.list_my_courses]
        studentDB.end()
        return self.list_my_courses
    
    def register_course(self,courseID,password):
        studentDB = DataBase()
        l= list(studentDB.execute(f"SELECT course_id FROM courses WHERE course_id = {courseID} AND password = '{password}'"))
        if( len(l) ==0):
            print("sorry wrong password of this course is not exist")
        else:
            ifexist = list(studentDB.execute(f"SELECT course_id FROM enrolled_course WHERE course_id = {courseID} AND user_id = '{self.id}'"))
            if len(ifexist)==0:
                studentDB.execute(f"INSERT INTO enrolled_course (course_ID,user_id,Account_type)VALUES({courseID},{self.id},{self.type_ID});")
            else:
                print("this registeration is already exist   ")
        studentDB.end()
    
    def coursesStudentInfo(self):
        self.studentCourses()
        res = []
        for i in self.list_my_courses:
            res.append(Course(i))
        return res

    def view_courses(self):
        result=[]
        try:
            self.studentCourses()
            studentDB = DataBase()
            s=convertToSqlTuple(self.list_my_courses)
            print(s)
            result = list(studentDB.execute(f"SELECT course_id ,name ,password FROM courses WHERE course_id NOT IN {s} "))
            studentDB.end()
            
        except:
            print("some of this data is incorrect")
        finally:
            return result
    
    def add_solution_on_this_assignment(self,AssignmentID,courseID,solution):
        self.studentCourses()
        if(courseID not in self.list_my_courses):
            print("you are not register in this course please try again ")
            return None
        
        studentDB = DataBase()
        ifThereIsSolutionsBefor = studentDB.execute(f"SELECT solution_id FROM solutions WHERE user_id = {self.id} AND Assignment_id = {AssignmentID}")
        ifThereIsSolutionsBefor = [i[0] for i in ifThereIsSolutionsBefor]
        
        if(len(ifThereIsSolutionsBefor)==0):
            studentDB.execute(f"INSERT INTO solutions (Assignment_id,user_id,solution)VALUES({AssignmentID},{self.id},'{solution}'); ")
        
        else:
            print("you have made submition befor the old one will be deleted :) ")
            studentDB.execute(f"UPDATE solutions SET Assignment_id = '{AssignmentID}', user_id = '{self.id}', solution = '{solution}' WHERE solution_id = '{ifThereIsSolutionsBefor[0]}' ")
        
        studentDB.end()
        print("solution has been submitted <<>> ")

    def unrigester_from_course(self,courseID):
        self.studentCourses()
        if(courseID not in self.list_my_courses):
            print("you are not registered in this course ??!!  ")
            return None
        studentDB = DataBase()
        studentDB.execute(f"DELETE FROM enrolled_course WHERE course_ID = {courseID} AND user_id = {self.id}")
        studentDB.end()
        pass
