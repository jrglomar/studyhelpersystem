import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                                        user='root',
                                        passwd='1234',
                                        database='studyhelper')
cursor = mydb.cursor()


class TestDb:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def read(self):
        
        print("Read")
        self.cursor = cursor
        self.mydb = mydb
        self.cursor = self.mydb.cursor()
        self.cursor.execute("select * from REMINDER WHERE StudentID = %s;", 
            (5, )
        )
        x = self.cursor.fetchall()
        print(x)
        
class Validation:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor
    
    def validationUserRegistration(self, username):
        try:
            self.cursor.execute("SELECT * FROM STUDENTS WHERE Username = %s;", username)
            return (self.cursor.fetchone())
        except:
            return False

class UserDb:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def userLogin(self, data):
        try:
            self.cursor.execute("SELECT * FROM students WHERE Username = %s AND Password = %s;", data)
            return (self.cursor.fetchone())
        except:
            return False

    def userRegistration(self, data, username):
        try:
            username = (username,)
            self.validation = Validation()
            reg = self.validation.validationUserRegistration(username)
            if reg:
                pass
            else:
                try:
                    self.cursor.execute("INSERT INTO STUDENTS(Username,Password) VALUES(%s, %s);", (data))
                    self.mydb.commit()
                except:
                    pass
            return reg
        except:
            return False

    def newTask(self, data):
            newTask = self.cursor.execute("INSERT INTO REMINDER(Type, Title, Due_Date, Details, StudentID) VALUES(%s, %s, %s, %s, %s);",
            (data))
            self.mydb.commit()

    def newType(self, data):
            self.cursor.execute("INSERT INTO REMINDERTYPE(Description) VALUES(%s);", 
            (data))
            self.mydb.commit()

    def getType(self):
            self.cursor.execute("SELECT Description FROM REMINDERTYPE;")
            x = self.cursor.fetchall()
            self.mydb.commit()
            
            return x
