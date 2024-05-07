import mysql.connector
import matplotlib.pyplot as plt
  
# Connecting with MySql
con = mysql.connector.connect(user='root', password='1234', host='localhost', database='mit')
	
# Using cursor() method to create cursor object
cursor = con.cursor()

sql = ("""SELECT date, SUM(sales) FROM mrts
WHERE id = "45111"
GROUP BY date;""")
cursor.execute(sql)

month1 = []
sales1 = []
for row in cursor.fetchall():
    month1.append(row[0])
    sales1.append(row[1])

sql = ("""SELECT date, SUM(sales) FROM mrts
WHERE id = "45112"
GROUP BY date;""")
cursor.execute(sql)

month2 = []
sales2 = []
for row in cursor.fetchall():
    month2.append(row[0])
    sales2.append(row[1])

sql = ("""SELECT date as y, SUM(sales) FROM mrts
WHERE  id = "451211"
GROUP BY date;""")
cursor.execute(sql)

month3 = []
sales3 = []
for row in cursor.fetchall():
    month3.append(row[0])
    sales3.append(row[1])

cursor.close()
con.close()

plt.plot(month1, sales1, label="Sporting good stores")
plt.plot(month2, sales2, label="Hobby, toy, and game stores")
plt.plot(month3, sales3, label="Book stores")

plt.xlabel('Year')
plt.ylabel('Sales in Millions of Dollars')
plt.title("Trends of question 3.3.3, Monthly")


plt.legend()

plt.show()