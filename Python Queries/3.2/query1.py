import mysql.connector

  
# Connecting with MySql
con = mysql.connector.connect(user='root', password='1234', host='localhost', database='mit')
	
# Using cursor() method to create cursor object
cursor = con.cursor()

sql = ("""
SELECT * FROM mrts
WHERE  status = "NaN";
""")
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)

cursor.close()
con.close()