import psycopg2 as pg2
conn=pg2.connect(database='dvdrental',user='postgres',password='anushka03')
curr=conn.cursor()
curr.execute('SELECT * FROM payment')
curr.fetchone()