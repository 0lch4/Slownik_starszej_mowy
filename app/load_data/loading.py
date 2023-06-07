import os
from app.connection.mydb import conn

mydb = conn()


def open_file(filename):
    return open(filename, "r", encoding="utf-8")


def create_tables():
    # iterates on all files in dictionaries folder
    for filename in os.listdir("dictionaries"):
        if filename.endswith(".txt"):
            # table name = file name
            tablename = os.path.splitext(filename)[0]
            mycursor = mydb.cursor()
            mycursor.execute(
                f"CREATE TABLE {tablename} (tlumaczenie VARCHAR(255), polskie_slowa TEXT)"
            )
            with open_file(os.path.join("dictionaries", filename)) as file:
                for line in file:
                    elf_word, polish_word = line.strip().split(" - ", 1)
                    sql = f"INSERT INTO {tablename} (tlumaczenie, polskie_slowa) VALUES (%s, %s)"
                    val = (elf_word, polish_word)
                    mycursor.execute(sql, val)

            mydb.commit()


if __name__ == "__main__":
    create_tables()
