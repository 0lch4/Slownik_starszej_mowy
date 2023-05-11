import os
from mydb import conn

mydb = conn()

def open_file(filename):
    return open(filename, 'r', encoding='utf-8')

def create_tables():
    for filename in os.listdir("slowniki"):
        if filename.endswith(".txt"):
            tablename = os.path.splitext(filename)[0]

            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE {} (tlumaczenie VARCHAR(255), polskie_slowa TEXT)".format(tablename))

            with open_file(os.path.join("slowniki", filename)) as file:
                for line in file:
                    slowo, tlumaczenie = line.strip().split(' - ', 1)
                    sql = "INSERT INTO {} (tlumaczenie, polskie_slowa) VALUES (%s, %s)".format(tablename)
                    val = (slowo, tlumaczenie)
                    mycursor.execute(sql, val)

            mydb.commit()
            print("Plik {} dodany do bazy".format(filename))
                       
if __name__ == '__main__':   
    create_tables()