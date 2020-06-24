import os
import pymysql

#Get username from gitpod Workspace
#(modify this if running on another environemt)
username = os.getenv('C9_USER')

#connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "Select * From Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close the connection , regardless of whether the above was successfull
    connection.close()