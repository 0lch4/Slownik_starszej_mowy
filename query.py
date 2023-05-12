from mydb import conn

mydb = conn()

#wysyla zapytanie do bazy o podane slowo
def query(word):
    tablename=word[:1]
    mycursor = mydb.cursor()
    sql = "SELECT * FROM {} WHERE polskie_slowa LIKE '{}';".format(tablename,word)
    print(sql)
    mycursor.execute(sql)
    #zwraca wartosc z bazy
    result = mycursor.fetchall()
    return result
