import sqlite3

class DataBase:
    sqlite3.connect("lib_SQL.db").cursor().execute("""
            create table if not exists users(
                id integer NOT NULL PRIMARY KEY,
                email VARCHAR(200) NOT NULL UNIQUE,
                fullName VARCHAR(200) NOT NULL,
                userName VARCHAR(200) NOT NULL UNIQUE,
                password VARCHAR(200) NOT NULL,
                type INTEGER,
                Accept_type INTEGER)""")

    sqlite3.connect("lib_SQL.db").cursor().execute("""
            create table if not exists courses(
                course_id integer NOT NULL PRIMARY KEY,
                name VARCHAR(200) NOT NULL,
                owner_id integer,
                password VARCHAR(200),
                dead_line date,
                FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE)""")


    sqlite3.connect("lib_SQL.db").cursor().execute("""
            create table if not exists requirment(
                course_id integer NOT NULL,
                requied_id integer NOT NULL,
                PRIMARY KEY(course_id,requied_id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (requied_id) REFERENCES courses(course_id) ON DELETE CASCADE ON UPDATE CASCADE)""")


    sqlite3.connect("lib_SQL.db").cursor().execute("""
            create table if not exists enrolled_course(
                course_ID integer NOT NULL,
                user_id integer NOT NULL,
                Account_type INTEGER, 
                PRIMARY KEY(course_ID,user_id),
                FOREIGN KEY (course_ID) REFERENCES courses(course_id) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE)""")
    
    sqlite3.connect("lib_SQL.db").cursor().execute("""
            create table if not exists Assignments(
                Assignment_id integer NOT NULL,
                course_ID integer NOT NULL,
                Assigment_question VARCHAR(200) NOT NULL,
                FullMark INTEGER NOT NULL, 
                Assigment_dead_line date NOT NULL,
                PRIMARY KEY(Assignment_id),
                FOREIGN KEY (course_ID) REFERENCES courses(course_id) ON DELETE CASCADE ON UPDATE CASCADE)""")


    sqlite3.connect("lib_SQL.db").cursor().execute("""
                create table if not exists solutions(
                    solution_id integer NOT NULL,
                    Assignment_id integer NOT NULL,
                    user_id integer NOT NULL,
                    solution VARCHAR(200) NOT NULL,
                    grade REAL NOT NULL,
                    comment VARCHAR(200) NOT NULL,
                    reat VARCHAR(200) NOT NULL,
                    PRIMARY KEY(solution_id),
                    FOREIGN KEY (Assignment_id) REFERENCES Assignments(Assignment_id) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE)""")


    sqlite3.connect("lib_SQL.db").cursor().execute("""
                create table if not exists Teacher(
                    user_id integer,
                    course_id integer,  
                    PRIMARY KEY(course_id,user_id),
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE ON UPDATE CASCADE)""")


    sqlite3.connect("lib_SQL.db").cursor().execute("""
                create table if not exists messages(
                    user_id integer,
                    reciever_id integer,
                    message_id integer,
                    message VARCHAR(200),
                    M_type integer,
                    PRIMARY KEY(message_id),
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,                
                    FOREIGN KEY (reciever_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
                    )""")

    sqlite3.connect("lib_SQL.db").cursor().execute("""
                create table if not exists Replay(
                    Replay_id integer not null,
                    message_id integer not null,
                    replayer_id integer not null,
                    replay_message VARCHAR(200) not null,
                    PRIMARY KEY(Replay_id),
                    FOREIGN KEY (message_id) REFERENCES messages(message_id) ON DELETE CASCADE ON UPDATE CASCADE)""")

    def __init__(self):
        self.conne=sqlite3.connect("lib_SQL.db")
        self.curs= self.conne.cursor()
        self.curs.execute("PRAGMA foriegn_keys = ON")

    def execute(self,statment):
        result=self.curs.execute(statment)
        self.conne.commit()
        return result
    def end(self):
        self.conne.close()


