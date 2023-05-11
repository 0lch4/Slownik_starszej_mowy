
from mydb import conn

mydb = conn()

def query(word):
    tablename=word[:1]
    mycursor = mydb.cursor()
    sql = "SELECT * FROM {} WHERE tlumaczenie LIKE '{}';".format(tablename,word)
    print(sql)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

if __name__ == '__main__':   
    word = 'zatoka'        
    result = query(word)
    print(result)