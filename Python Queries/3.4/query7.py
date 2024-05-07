import mysql.connector
import matplotlib.pyplot as plt
  
# Connecting with MySql
con = mysql.connector.connect(user='root', password='1234', host='localhost', database='mit')
	
# Using cursor() method to create cursor object
cursor = con.cursor()

# The information brought by the query is fetched into the following variables:
sql = ("""SELECT b.y,
(cast(b.sales-a.sales as float)/a.sales*100) as PctChange
FROM (SELECT Year(date) as y, SUM(sales) as sales FROM mrts
WHERE id = "44811" AND date NOT LIKE "%2021-%"
GROUP BY y) a 
LEFT JOIN (SELECT Year(date) as y, SUM(sales) as sales FROM mrts
WHERE id = "44811" AND date NOT LIKE "%2021-%"
GROUP BY y) b
ON (a.y + 1 = b.y)
ORDER BY a.y; """)
cursor.execute(sql)

# The query is written
year1 = []
sales1 = []
for row in cursor.fetchall():
    year1.append(row[0])
    sales1.append(row[1])

# The query is written
sql = ("""SELECT b.y,
(cast(b.sales-a.sales as float)/a.sales*100) as PctChange
FROM (SELECT Year(date) as y, SUM(sales) as sales FROM mrts
WHERE id = "44812" AND date NOT LIKE "%2021-%"
GROUP BY y) a 
LEFT JOIN (SELECT Year(date) as y, SUM(sales) as sales FROM mrts
WHERE id = "44812" AND date NOT LIKE "%2021-%"
GROUP BY y) b
ON (a.y + 1 = b.y)
ORDER BY a.y; """)
cursor.execute(sql)

# The information brought by the query is fetched into the following variables:
year2 = []
sales2 = []
for row in cursor.fetchall():
    year2.append(row[0])
    sales2.append(row[1])


cursor.close()
con.close()

# A graph showing the data is plotted.

plt.plot(year1, sales1, label="Men's Clothing")
plt.plot(year2, sales2, label="Women's Clothing")

plt.xlabel('Year')
plt.ylabel('Percentage Change (%)')
plt.title("Clothing Percentage Change By Year")


plt.legend()

plt.show()

