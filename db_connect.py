import mysql.connector
import config_read

#To conect to Mysql database
db_connection = mysql.connector.connect(**config_read.config_file['mysql'])

#Check mysql database connection
if not db_connection.is_connected:
    print("Mysql Connection failed")
else:
    print("Success")

    
    

