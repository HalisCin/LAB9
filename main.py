import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Halis650."
)
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS MyNewDatabase")

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = 'MyNewDatabase',
    passwd = "Halis650.")

if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database='MyNewDatabase',
        passwd="Halis650.")

    mySql_Create_Table_Query = """ CREATE TABLE IF NOT EXISTS MyMovieTable(
                                    Id int(40) NOT NULL,
                                    Movie VARCHAR(50) NOT NULL,
                                    Date VARCHAR(50) NOT NULL,
                                    MCU_Phase VARCHAR(50))"""
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("MyMovieTable created successfully")

    path = open("C:\\Users\\halis\\Desktop\\Marvel.txt",'r')

    mysql_insert_query = """ INSERT INTO MyMovieTable (Id, Movie, Date,
                                                  MCU_Phase) VALUES(%s,%s,%s,%s)"""

    while path:
        marvel = path.readline()
        if marvel == "":
            break
        splitLines = marvel.split()
        mysql_insert_query = """INSERT INTO Marvel(ID,MOVIE,DATE,MCU_PHASE) VALUES (%s,%s,%s,%s)"""
        record = (splitLines[0], splitLines[1], splitLines[2], splitLines[3])
        cursor.execute(mysql_insert_query, record)
        dataBase.commit()

    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into MyMovieTable")


    query = "SELECT * FROM Marvel"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


    q = "DELETE FROM Marvel WHERE MOVIE = 'TheIncredibleHulk'"
    cursor.execute(q)
    dataBase.commit()


    query = "SELECT * FROM Marvel WHERE MCU_PHASE = 'Phase2'"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


    query = "UPDATE Marvel SET DATE = 'November3,2017' WHERE MOVIE = 'Thor:Ragnarok'"
    cursor.execute(query)
    dataBase.commit()


except mysql.connector.Error as error:
    print("Something went wrong in MySQL: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")