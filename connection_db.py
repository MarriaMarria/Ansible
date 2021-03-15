import psycopg2
# postgres cnnection
host = 'localhost'
dbname = "postgres"
user = 'maria'
password = 'password'

conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)
print("connection established")
cursor = conn.cursor()

def create_table():
    cursor.execute("DROP TABLE testing")
    cursor.execute("CREATE TABLE IF NOT EXISTS testing (id INT PRIMARY KEY, name VARCHAR(50))")
    conn.commit()
    print("table created")

create_table()

def insert_to(): 
    cursor.execute("INSERT INTO testing VALUES (%s)", ("1"))
    conn.commit()
    print('inserted')

insert_to()
