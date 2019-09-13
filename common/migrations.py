import time

import psycopg2


time.sleep(3)


connection = psycopg2.connect(
            user="admin",
            password="admin_pass",
            host="db",
            port="5432",
            dbname="pg_core_db"
        )
cursor = connection.cursor()

cursor.execute(
         '''CREATE TABLE IF NOT EXISTS rate
                  (pair text PRIMARY KEY, price DECIMAL(10, 5))'''
     )

connection.commit()
cursor.close()
connection.close()
