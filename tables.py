from estd_connection import estd_connection

cursor = estd_connection()

cursor.execute("DROP TABLE IF EXISTS STUDENT")

sql = """
CREATE TABLE STUDENT(
ID VARCHAR(20),
NAME VARCHAR(100),
DEPARTMENT VARCHAR(100)
);
"""

cursor.execute(sql)
print("Table created successfully")