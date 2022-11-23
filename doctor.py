from teacher import Teacher
from database import DataBase
from course import Course
from Assignment import Assignment
class Doctor(Teacher):
    def __init__(self, id, email, full_name, user_name, type_ID, admin_accept):
        super().__init__(id, email, full_name, user_name, type_ID, admin_accept)

    def createCourse(self,name,password,dead_line):
        # date_entry = input('Enter a date in YYYY-MM-DD format')
        # year, month, day = map(int, date_entry.split('-'))
        # date1 = datetime.date(year, month, day)
        doctorDB = DataBase()
        doctorDB.execute(f"INSERT INTO courses (name,owner_id,password,dead_line)VALUES('{name}',{self.id},'{password}','{dead_line}');")
        doctorDB.end()
        pass
    
    def delete_course(self,courseID):
        self.coursesList()
        if(courseID not in self.courses_list):
            print("sorry this course is not for you ")
            return  None
        Course(courseID).deleteCourse()
        print(f"course with id = {courseID} has been deleted")
        
    def sendRequestToTeacherAssistent(self,courseID):
        TAID = int(input("enter Teacher Assistent ID : "))
        DoctorDB = DataBase()
        DoctorDB.execute(f"INSERT INTO Teacher (user_id,course_id) VALUES ({TAID},{courseID})")
        DoctorDB.end()
        pass

