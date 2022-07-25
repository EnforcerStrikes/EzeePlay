import mysql.connector as mysql
import datetime   
format_str = '%Y-%m-%d' 

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""  # Enter mySQL password
)
c = db.cursor()

# Initialise
query = "DROP DATABASE IF EXISTS SCB"
c.execute(query)
query = "CREATE DATABASE SCB"
c.execute(query)
query = "USE SCB"
c.execute(query)

# Tables
query = "CREATE TABLE RESIDENTS( FLAT VARCHAR (5) PRIMARY KEY NOT NULL, NAME VARCHAR (15) NOT NULL, NUMBER VARCHAR (10) NOT NULL, BUILDING VARCHAR (15) NOT NULL);"
c.execute(query)
query = "CREATE TABLE SPORTS_LIST( SPORT VARCHAR (15) PRIMARY KEY NOT NULL, PRICE INT (5) NOT NULL, SLOTS INT (2) NOT NULL);"
c.execute(query)
query = "CREATE TABLE BOOKING( ID INT(11) NOT NULL AUTO_INCREMENT, FLAT VARCHAR (5) NOT NULL, SPORT VARCHAR (15) NOT NULL, DATE DATE NOT NULL, TIME_SLOT VARCHAR (15) NOT NULL, FOREIGN KEY (FLAT) REFERENCES RESIDENTS(FLAT), PRIMARY KEY (ID), FOREIGN KEY (SPORT) REFERENCES SPORTS_LIST(SPORT))"
c.execute(query)

# Dummy Residents
query = '''INSERT INTO RESIDENTS (FLAT, NAME, NUMBER, BUILDING) VALUES (%s, %s, %s, %s)'''
values = ("L1004", "Pranav Parker", "9811928778", "Lily")
c.execute(query, values)
query = '''INSERT INTO RESIDENTS (FLAT, NAME, NUMBER, BUILDING) VALUES (%s, %s, %s, %s)'''
values = ("R0601", "Meet Kulkarni", "7309072668", "Rose")
c.execute(query, values)
query = '''INSERT INTO RESIDENTS (FLAT, NAME, NUMBER, BUILDING) VALUES (%s, %s, %s, %s)'''
values = ("J0203", "Akshita Singh", "9830583772", "Jasmine")
c.execute(query, values)
query = '''INSERT INTO RESIDENTS (FLAT, NAME, NUMBER, BUILDING) VALUES (%s, %s, %s, %s)'''
values = ("D2302", "Rohit Sagar", "8377269006", "Daisy")
c.execute(query, values)
query = '''INSERT INTO RESIDENTS (FLAT, NAME, NUMBER, BUILDING) VALUES (%s, %s, %s, %s)'''
values = ("R1304", "Raj Shetty", "8832751118", "Rose")
c.execute(query, values)
query = '''INSERT INTO RESIDENTS (FLAT, NAME, NUMBER, BUILDING) VALUES (%s, %s, %s, %s)'''
values = ("J1901", "Riya Agarwal", "6308346887", "Jasmine")
c.execute(query, values)

# Dummy Sports
query = '''INSERT INTO SPORTS_LIST (SPORT, PRICE, SLOTS) VALUES (%s, %s, %s)'''
values = ("Football", "1500", "1")
c.execute(query, values)
query = '''INSERT INTO SPORTS_LIST (SPORT, PRICE, SLOTS) VALUES (%s, %s, %s)'''
values = ("Cricket", "1200", "1")
c.execute(query, values)
query = '''INSERT INTO SPORTS_LIST (SPORT, PRICE, SLOTS) VALUES (%s, %s, %s)'''
values = ("Table Tennis", "100", "3")
c.execute(query, values)
query = '''INSERT INTO SPORTS_LIST (SPORT, PRICE, SLOTS) VALUES (%s, %s, %s)'''
values = ("Lawn Tennis", "300", "2")
c.execute(query, values)
query = '''INSERT INTO SPORTS_LIST (SPORT, PRICE, SLOTS) VALUES (%s, %s, %s)'''
values = ("Billiards", "500", "2")
c.execute(query, values)
query = '''INSERT INTO SPORTS_LIST (SPORT, PRICE, SLOTS) VALUES (%s, %s, %s)'''
values = ("Carrom", "10", "4")
c.execute(query, values)
query = '''INSERT INTO SPORTS_LIST (SPORT, PRICE, SLOTS) VALUES (%s, %s, %s)'''
values = ("Chess", "10", "4")
c.execute(query, values)
query = '''INSERT INTO SPORTS_LIST (SPORT, PRICE, SLOTS) VALUES (%s, %s, %s)'''
values = ("Basketball", "1500", "2")
c.execute(query, values)

# Dummy Entries
date_str = '2021-12-25' 
datetime_obj = datetime.datetime.strptime(date_str, format_str)
query = '''INSERT INTO BOOKING (FLAT, SPORT, DATE, TIME_SLOT) VALUES (%s, %s, %s, %s)'''
values = ("J1901", "Football", datetime_obj, "9 AM to 11 AM") 
c.execute(query, values)

date_str = '2021-11-5' 
datetime_obj = datetime.datetime.strptime(date_str, format_str)
query = '''INSERT INTO BOOKING (FLAT, SPORT, DATE, TIME_SLOT) VALUES (%s, %s, %s, %s)'''
values = ("L1004", "Table Tennis", datetime_obj, "6 PM to 8 PM") 
c.execute(query, values)

date_str = '2021-10-23' 
datetime_obj = datetime.datetime.strptime(date_str, format_str)
query = '''INSERT INTO BOOKING (FLAT, SPORT, DATE, TIME_SLOT) VALUES (%s, %s, %s, %s)'''
values = ("R0601", "Cricket", datetime_obj, "4 PM to 5 PM") 
c.execute(query, values)

date_str = '2021-10-27' 
datetime_obj = datetime.datetime.strptime(date_str, format_str)
query = '''INSERT INTO BOOKING (FLAT, SPORT, DATE, TIME_SLOT) VALUES (%s, %s, %s, %s)'''
values = ("J0203", "Table Tennis", datetime_obj, "12 PM to 3 PM") 
c.execute(query, values)

date_str = '2021-10-30' 
datetime_obj = datetime.datetime.strptime(date_str, format_str)
query = '''INSERT INTO BOOKING (FLAT, SPORT, DATE, TIME_SLOT) VALUES (%s, %s, %s, %s)'''
values = ("J1901", "Lawn Tennis", datetime_obj, "9 PM to 10 PM") 
c.execute(query, values)

date_str = '2021-11-2' 
datetime_obj = datetime.datetime.strptime(date_str, format_str)
query = '''INSERT INTO BOOKING (FLAT, SPORT, DATE, TIME_SLOT) VALUES (%s, %s, %s, %s)'''
values = ("R1304", "Basketball", datetime_obj, "7 AM to 10 AM") 
c.execute(query, values)

date_str = '2021-6-5' 
datetime_obj = datetime.datetime.strptime(date_str, format_str)
query = '''INSERT INTO BOOKING (FLAT, SPORT, DATE, TIME_SLOT) VALUES (%s, %s, %s, %s)'''
values = ("D2302", "Billiards", datetime_obj, "10 PM to 11 PM") 
c.execute(query, values)

# c.execute("SELECT * FROM BOOKING")
# play=c.fetchall()
# for i in play:
#   print(i[3])



db.commit()
db.close()

