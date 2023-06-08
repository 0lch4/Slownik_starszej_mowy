from .mydb import conn

mydb = conn()


def query(word: str) -> str:
    tablename = word[:1]
    mycursor = mydb.cursor()
    sql = f"SELECT * FROM {tablename} WHERE polskie_slowa LIKE '{word}';"  # noqa: S608
    print(sql)
    mycursor.execute(sql)
    return  mycursor.fetchall()
