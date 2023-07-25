import pandas as pd
import numpy as np
import psycopg2
#forming the connection
conn = psycopg2.connect(
    database="testdb",#enter your database name
    user='postgres',#enter your postgres username
    password='1234567890',#enter your password
    host='localhost',#enter your host name
    port='5432'#port number
)
cursor = conn.cursor()
cursor.execute("select * from public.employee")
rows = cursor.fetchall()
# cursor.execute("INSERT INTO public.employee(emp_id, first_name, last_name, age, gender, income, dept, address)VALUES (102, 'Obulu', 'Polimera', 58,'M', 1200, 'Front End', 'HYD')")
# cursor.execute("UPDATE public.employee SET emp_id=102, first_name='Pramod__Kumar', last_name='__Devarakonda', age=23, gender='M', income=10000, dept='Testing', address='HYD' WHERE emp_id=102")
# cursor.execute("DELETE FROM public.employee	WHERE emp_id = 102")
conn.commit()
cursor.close()
conn.close()
print (rows)

# import psycopg2

# from psycopg2 import Error

# from sqlalchemy import create_engine ,Column,Integer,String

# from sqlalchemy.orm import sessionmaker




# DATABASE_URL = 'postgresql://postgres:1234567890@localhost:5432/testdb'

# engine = create_engine(DATABASE_URL, echo = True)

# Session = sessionmaker(bind = engine)
