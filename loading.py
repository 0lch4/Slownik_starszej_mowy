import os
from mydb import conn
#polaczenie z bazą danych
mydb = conn()
#latwiejsze otwieranie wielu plików
def open_file(filename):
    return open(filename, 'r', encoding='utf-8')
#tworzy tabele w bazie wraz z zawartością
def create_tables():
    #iteruje po wszystkich plikach w folderze dictonaries
    for filename in os.listdir("dictonaries"):
        if filename.endswith(".txt"):
            #nazwa tabeli to nazwa pliku
            tablename = os.path.splitext(filename)[0]
            #tworzenie kursora
            mycursor = mydb.cursor()
            #tworzenie tabeli o nazwie pliku
            mycursor.execute("CREATE TABLE {} (tlumaczenie VARCHAR(255), polskie_slowa TEXT)".format(tablename))
            #otwiercie wszystkich plikow w katalogu
            with open_file(os.path.join("dictonaries", filename)) as file:
                #dodawanie wartosci w odpowiednich miejscach
                for line in file:
                    elf_word, polish_word = line.strip().split(' - ', 1)
                    sql = "INSERT INTO {} (tlumaczenie, polskie_slowa) VALUES (%s, %s)".format(tablename)
                    val = (elf_word, polish_word)
                    mycursor.execute(sql, val)

            mydb.commit()
            
#aby ta czesc nie wykonywala sie podczas importu                        
if __name__ == '__main__':   
    create_tables()