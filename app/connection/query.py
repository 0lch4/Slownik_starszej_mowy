from app.connection.mydb import conn

mydb = conn()


def query(word):
    tablename = word[:1]
    mycursor = mydb.cursor()
    sql = "SELECT * FROM {} WHERE polskie_slowa LIKE '{}';".format(tablename, word)
    print(sql)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result
