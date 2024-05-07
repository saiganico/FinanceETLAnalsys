import mysql.connector
import csv

  
# Connection is created with the database
con = mysql.connector.connect(user='root', password='1234', host='localhost', database='mit')
	
# A cursor is instanced
cursor = con.cursor()

# The table is dropped in case it exists.
cursor.execute("DROP TABLE IF EXISTS MRTS")

# A query is written to create the table within the database.
sql_query ='''CREATE TABLE MRTS(
   id VARCHAR(25) NOT NULL,
   id_group INT NOT NULL,
   business_description VARCHAR(100),
   date DATE NOT NULL,
   sales INT NULL,
   status VARCHAR(20) NOT NULL
  )'''

# The query is executed.
cursor.execute(sql_query)
print("Table created successfully")

cursor = con.cursor()

# The CSV file is read to load it into the database.
with open("data/transformedmrtsales92-present.csv", mode='r') as csv_data:
    reader = csv.reader(csv_data, delimiter=',')
    # The header is ignored when uploaded into the database.
    next(reader, None)
    csv_data_list = list(reader)
    for row in csv_data_list:
      # The NaN values, converted by Pandas into an empty string, are specified as None values into the database.
      for i in range(len(row)):
          if row[i] == '':
              row[i] = None        
      # The query that inserts the dataset into the database is executed.
      cursor.execute("""
                  INSERT INTO MRTS(
                  id, id_group, business_description, date, sales, status)
                  VALUES(%s,%s,%s,%s,%s,%s)""",
                  (row[0], row[1], row[2], row[3], row[4], row[5]))
con.commit()
cursor.close()
con.close()
print("Done")

