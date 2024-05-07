import mysql.connector
import matplotlib.pyplot as plt
  
# Connecting with MySql
con = mysql.connector.connect(user='root', password='1234', host='localhost', database='mit')
	
# Using cursor() method to create cursor object
cursor = con.cursor()

# The query is written
sql = """SELECT
    date,
    sales/(AVG(sales) OVER(PARTITION BY YEAR(date))) * 100 - 100 as month_comparison_avg,
    sales/(SUM(sales) OVER(PARTITION BY YEAR(date))) * 100 as month_contribution
FROM mrts
WHERE id = "448" AND date like "%2018%";"""
cursor.execute(sql)

# The information brought by the query is fetched into the following variables:
date = []
month_comparison = []
month_contribution = []
for row in cursor.fetchall():
    date.append(row[0])
    month_comparison.append(row[1])
    month_contribution.append(row[2])

# A graph showing the data is plotted.
plt.plot(date, month_comparison, label="Month Percentage vs Month Average")
plt.plot(date, month_contribution, label="Month Sale Percentage")

plt.xlabel('Year')
plt.ylabel('Percentage (%)')
plt.title("Clothing Sales - 2018")


plt.legend()

plt.show()