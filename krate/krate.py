from db import DbManager
from db.PgSqlDbManager import PgSqlDbManager

class Krate:
    @staticmethod
    def do_something():
        print "Hello World"
        
x = PgSqlDbManager(hostname="localhost", username="rohan", password="k1l1m1nj4r0", port=5432, database='pg_general')
x.connect()
y = x.run_query('SELECT * FROM film')

for m in y.fetchall():
    print m

