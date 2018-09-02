import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","14CS10060","btech14","14CS10060" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
# cursor.execute("SELECT VERSION()")


""" 
for creating tables if not present and inserting values.I have commented it out as in my database all created tables are present.




cursor.execute("CREATE TABLE STUDENT(NAME VARCHAR(100),ROLLNUMBER VARCHAR(10), ADDRESS VARCHAR(200), DEPARTMENT VARCHAR(20));")
cursor.execute("CREATE TABLE COURSE(COURSEID VARCHAR(10),COURSENAME VARCHAR(50),DEPARTMENT VARCHAR(20));")
cursor.execute("CREATE TABLE EXAMINATION(COURSEID VARCHAR(10),EXAM_TYPE VARCHAR(20),DATE DATE,FULL_MARKS NUMERIC(3));")
cursor.execute("CREATE TABLE REGISTRATION(ROLLNUMBER VARCHAR(10),COURSEID VARCHAR(10));")
cursor.execute("CREATE TABLE GRADECARD(GRADE CHAR(2),MARKS NUMERIC(5),COURSEID VARCHAR(10),ROLLNUMBER VARCHAR(10));")
cursor.execute("CREATE TABLE TEACHER(TEACHERID VARCHAR(10),TEACHER_NAME VARCHAR(100),DEPARTMENT VARCHAR(20));")
cursor.execute("CREATE TABLE TEACHES(TEACHERID VARCHAR(10),COURSEID VARCHAR(10),SLOTID VARCHAR(1),ROOMNO VARCHAR(5));")
cursor.execute("CREATE TABLE TIMING(SLOTID VARCHAR(1),DAY VARCHAR(10),START_TIME VARCHAR(10),END_TIME VARCHAR(10));")
cursor.execute("CREATE TABLE CLASSROOM(ROOMNO VARCHAR(5), CLASS_CAPACITY NUMERIC(3));")


cursor.execute("INSERT INTO STUDENT VALUES ('RAM','14CS10080','KHARAGPUR','CSE'),('RIK','14ME10081','KHARAGPUR','ME'),('TOM','14CS10088','BHAGALPUR','CSE'),('ROGER','14CS10085','DURGAPUR','CSE'),('SITA','14CS10077','KOLKATA','CSE');")
cursor.execute("INSERT INTO COURSE VALUES('CS60105','ADVANCED ALGORITHMS','CS'),('CS30106','DBMS','CS'),('CS61205','CRYPTOGRAPHY','CS');")
cursor.execute("INSERT INTO EXAMINATION VALUES('CS60105','MIDSEM','2016-03-01',100),('CS60105','ENDSEM','2016-05-01',100),('CS61205','MIDSEM','2016-03-04',100),('CS30106','MIDSEM','2016-02-04',100);")
cursor.execute("INSERT INTO REGISTRATION VALUES('14CS10080','CS60105'),('14CS10080','CS61205'),('14CS10080','CS30106'),('14CS10088','CS60105'),('14CS10085','CS60105'),('14CS10077','CS60105'),('14CS10088','CS61205'),('14CS10088','CS30106'),('14CS10085','CS61205');")
cursor.execute("INSERT INTO GRADECARD VALUES('EX',92,'CS60105','14CS10080'),('A',82,'CS61205','14CS10080'),('EX',94,'CS30106','14CS10080'),('B',70,'CS60105','14CS10088'),('EX',92,'CS61205','14CS10088'),('EX',92,'CS30106','14CS10088'),('P',42,'CS60105','14CS10085'),('F',20,'CS60105','14CS10077'),('C',62,'CS61205','14CS10077'),('D',52,'CS30106','14CS10085');")
cursor.execute("INSERT INTO TEACHER VALUES('CS100','PPC','CS'),('CS105','PPD','CS'),('CS110','PM','CS');")
cursor.execute("INSERT INTO TEACHES VALUES('CS100','CS30106','A','NC142'),('CS100','CS60105','B','NC142'),('CS110','CS30106','A','NC142');")
cursor.execute("INSERT INTO TIMING VALUES('A','MONDAY','08:00:00','09:00:00'),('B','MONDAY','09:00:00','10:00:00');")
cursor.execute("INSERT INTO CLASSROOM VALUES('NC142',100);")


"""


print "All  courses taught by PPC"
cursor.execute("SELECT COURSENAME FROM COURSE,TEACHES,TEACHER WHERE TEACHER.TEACHER_NAME='PPC'  AND  COURSE.COURSEID=TEACHES.COURSEID AND TEACHES.TEACHERID=TEACHER.TEACHERID;")
results = cursor.fetchall()

widths = []
columns = []
tavnit = '|'
separator = '+' 

for cd in cursor.description:
    widths.append(max(cd[2], len(cd[0])))
    columns.append(cd[0])

for w in widths:
    tavnit += " %-"+"%ss |" % (w,)
    separator += '-'*w + '--+'

print(separator)
print(tavnit % tuple(columns))
print(separator)
for row in results:
    print(tavnit % row)
print(separator)
print "\n"

print "All students registered in the courses taught by PPC"
cursor.execute("SELECT DISTINCT STUDENT.ROLLNUMBER,NAME FROM STUDENT,REGISTRATION,COURSE,TEACHES,TEACHER WHERE TEACHER.TEACHER_NAME='PPC'  AND  COURSE.COURSEID=TEACHES.COURSEID AND TEACHES.TEACHERID=TEACHER.TEACHERID  AND STUDENT.ROLLNUMBER=REGISTRATION.ROLLNUMBER AND REGISTRATION.COURSEID=COURSE.COURSEID;")
results = cursor.fetchall()

widths = []
columns = []
tavnit = '|'
separator = '+' 

for cd in cursor.description:
    widths.append(max(cd[2], len(cd[0])))
    columns.append(cd[0])

for w in widths:
    tavnit += " %-"+"%ss |" % (w,)
    separator += '-'*w + '--+'

print(separator)
print(tavnit % tuple(columns))
print(separator)
for row in results:
    print(tavnit % row)
print(separator)
print "\n"

print "The timings of all courses in Class-Room NC142."


cursor.execute("SELECT DISTINCT COURSE.COURSEID,COURSENAME,START_TIME,END_TIME,DAY FROM TIMING,TEACHES,CLASSROOM,COURSE WHERE CLASSROOM.ROOMNO='NC142' AND CLASSROOM.ROOMNO=TEACHES.ROOMNO AND TEACHES.SLOTID=TIMING.SLOTID AND TEACHES.COURSEID=COURSE.COURSEID;")
results = cursor.fetchall()

widths = []
columns = []
tavnit = '|'
separator = '+' 

for cd in cursor.description:
    widths.append(max(cd[2], len(cd[0])))
    columns.append(cd[0])

for w in widths:
    tavnit += " %-"+"%ss |" % (w,)
    separator += '-'*w + '--+'

print(separator)
print(tavnit % tuple(columns))
print(separator)
for row in results:
    print(tavnit % row)
print(separator)
print "\n"

print " The name of the students who received the highest marks in the courses taught by PPC"
cursor.execute("SELECT DISTINCT NAME FROM((SELECT NAME,GRADECARD.ROLLNUMBER FROM(SELECT COURSE.COURSEID,MAX(MARKS) AS MAXMARKS FROM STUDENT,REGISTRATION,COURSE,TEACHES,TEACHER,GRADECARD WHERE TEACHER.TEACHER_NAME='PPC' AND GRADECARD.ROLLNUMBER=REGISTRATION.ROLLNUMBER AND  COURSE.COURSEID=TEACHES.COURSEID AND TEACHES.TEACHERID=TEACHER.TEACHERID AND STUDENT.ROLLNUMBER=REGISTRATION.ROLLNUMBER AND REGISTRATION.COURSEID=COURSE.COURSEID AND COURSE.COURSEID=GRADECARD.COURSEID GROUP BY COURSE.COURSEID ) AS T,REGISTRATION,GRADECARD,STUDENT  WHERE T.COURSEID=REGISTRATION.COURSEID AND T.MAXMARKS=GRADECARD.MARKS AND GRADECARD.ROLLNUMBER=REGISTRATION.ROLLNUMBER AND STUDENT.ROLLNUMBER=REGISTRATION.ROLLNUMBER) AS T1);")
results = cursor.fetchall()

widths = []
columns = []
tavnit = '|'
separator = '+' 

for cd in cursor.description:
    widths.append(max(cd[2], len(cd[0])))
    columns.append(cd[0])

for w in widths:
    tavnit += " %-"+"%ss |" % (w,)
    separator += '-'*w + '--+'

print(separator)
print(tavnit % tuple(columns))
print(separator)
for row in results:
    print(tavnit % row)
print(separator)
print "\n"

print "The students who have received a grade of EX in the largest number of course"
cursor.execute("SELECT NAME,STUDENT.ROLLNUMBER FROM (SELECT MAX(NO_OF_EX) AS MAX_EX FROM (SELECT COUNT(*)AS NO_OF_EX,GRADECARD.ROLLNUMBER AS ROLLNO FROM GRADECARD WHERE GRADE='EX'GROUP BY GRADECARD.ROLLNUMBER ) AS T,STUDENT WHERE T.ROLLNO=STUDENT.ROLLNUMBER) AS T1,(SELECT COUNT(DISTINCT COURSEID)AS NO_OF_EX,GRADECARD.ROLLNUMBER AS ROLLNO FROM GRADECARD WHERE GRADE='EX' GROUP BY GRADECARD.ROLLNUMBER ) AS T2,STUDENT WHERE STUDENT.ROLLNUMBER=T2.ROLLNO AND T2.NO_OF_EX=T1.MAX_EX;")
results = cursor.fetchall()

widths = []
columns = []
tavnit = '|'
separator = '+' 

for cd in cursor.description:
    widths.append(max(cd[2], len(cd[0])))
    columns.append(cd[0])

for w in widths:
    tavnit += " %-"+"%ss |" % (w,)
    separator += '-'*w + '--+'

print(separator)
print(tavnit % tuple(columns))
print(separator)
for row in results:
    print(tavnit % row)
print(separator)
print "\n\n\n"
# disconnect from server
db.close()







