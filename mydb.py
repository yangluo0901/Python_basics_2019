import pymysql

# db = pymysql.connect(host="localhost",
#                      port=3306,
#                      user="root",
#                      passwd="root",
#                      db="test",
#                      charset="utf8",
#                      cursorclass=pymysql.cursors.DictCursor)
# # if add cursorclass=pymysql.cursors.DictCursor, return result as a dictionary
# try:
#     with db.cursor() as cursor:
#         sql = "SELECT * FROM person"
#         cursor.execute(sql)
#         result = cursor.fetchone()
#         print(result)
# finally:
#     db.close()

'''  CRUD  '''

conn = pymysql.connect(host="localhost",
                       user="root",
                       port=3306,
                       passwd="root",
                       charset="utf8")
CREATE_DB = "CREATE DATABASE Registration "
CREATE_TABLE = "CREATE TABLE {} ({})"
INSERT_DATA = "INSERT INTO {} ({}) VALUES ({})"
UPDATE_DATA = "UPDATE {} SET {} = {} WHERE {} = {}"
DELETE_DATA = "DELETE FROM {} WHERE {} = {}"
JOIN = "SELECT"
print(INSERT_DATA.format("Registration.Students", "first_name, last_name", "'Yang', 'Luo'"))
try:
    with conn.cursor() as mycursor:
        mycursor.execute("DROP DATABASE IF EXISTS Registration")
        mycursor.execute(CREATE_DB)  # create a database
        mycursor.execute("DROP TABLE IF EXISTS Registration.Students")
        mycursor.execute("DROP TABLE IF EXISTS Registration.Courses")
        #create tables
        mycursor.execute(CREATE_TABLE.format("Registration.Students",
                                             '''id int NOT NULL AUTO_INCREMENT,
                                            first_name VARCHAR(45) NOT NULL, 
                                            last_name VARCHAR(45) NOT NULL,
                                            PRIMARY KEY (id)'''))
        mycursor.execute(CREATE_TABLE.format("Registration.Courses",
                                             '''id int NOT NULL AUTO_INCREMENT,
                                            course_name VARCHAR(45) NOT NULL,
                                            major VARCHAR(45) NOT NULL,
                                            PRIMARY KEY (id)'''))
        # insert data
        mycursor.execute(INSERT_DATA.format("Registration.Students", "first_name, last_name", "'Yang', 'Luo'"))
        mycursor.execute(INSERT_DATA.format("Registration.Students", "first_name, last_name", "'Ran', 'Li'"))
        mycursor.execute(INSERT_DATA.format("registration.Courses",
                                            "course_name, major",
                                            "'Mechanical Design', 'Mechanical Engineering'"))
        mycursor.execute(INSERT_DATA.format("Registration.Courses",
                                            "course_name, major",
                                            "'Behavior Analysis' , 'Social Work' "))
        mycursor.execute(INSERT_DATA.format("Registration.Courses",
                                            "course_name, major",
                                            "'Exercise', 'Sports'"))
        mycursor.execute(INSERT_DATA.format("Registration.Courses",
                                            "course_name, major",
                                            "'To be Deleted', 'I dont care'"))
        # update
        mycursor.execute(UPDATE_DATA.format("Registration.Courses", "course_name", "'Gymnastics'", "id", "3"))

        # Delete
        mycursor.execute(DELETE_DATA.format("Registration.Courses", "course_name", "'To be Deleted'"))
        conn.commit()

finally:
    conn.close()
