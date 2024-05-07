import mysql.connector
import matplotlib.pyplot as plt
  
# Connecting with MySql
con = mysql.connector.connect(user='root', password='1234', host='localhost', database='mit')
	
# Using cursor() method to create cursor object
cursor = con.cursor()

# The query is written
sql = ("""SELECT date, SUM(sales) FROM mrts
WHERE id = "45111" AND date like "%-01-%"
GROUP BY date;""")
cursor.execute(sql)

# The information brought by the query is fetched into the following variables:
year1 = []
sales1 = []
for row in cursor.fetchall():
    year1.append(row[0])
    sales1.append(row[1])

# The query is written
sql = ("""SELECT date, SUM(sales) FROM mrts
WHERE id = "45112" AND date LIKE "%-01-%"
GROUP BY date;""")
cursor.execute(sql)
# The information brought by the query is fetched into the following variables:
year2 = []
sales2 = []
for row in cursor.fetchall():
    year2.append(row[0])
    sales2.append(row[1])

# The query is written
sql = ("""SELECT date, SUM(sales) FROM mrts
WHERE  id = "451211" AND date LIKE "%-01-%"
GROUP BY date;""")
cursor.execute(sql)

# The information brought by the query is fetched into the following variables:
year3 = []
sales3 = []
for row in cursor.fetchall():
    year3.append(row[0])
    sales3.append(row[1])

cursor.close()
con.close()

# A graph showing the data is plotted
plt.plot(year1, sales1, label="Sporting good stores")
plt.plot(year2, sales2, label="Hobby, toy, and game stores")
plt.plot(year3, sales3, label="Book stores")

plt.xlabel('Year')
plt.ylabel('Sales in Millions of Dollars')
plt.title("Trends of question 3.3.3, by January")


plt.legend()

plt.show()