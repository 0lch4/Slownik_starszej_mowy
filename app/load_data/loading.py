import os
from pathlib import Path
from app.connection.mydb import conn

mydb = conn()


def create_tables() -> None:
    # iterates on all files in dictionaries folder
    for filename in os.listdir("app/load_data/dictionaries"):
        if filename.endswith(".txt"):
            # table name = file name
            tablename = os.path.splitext(filename)[0]  # noqa: PTH122
            mycursor = mydb.cursor()
            mycursor.execute(
                f"CREATE TABLE {tablename} (tlumaczenie VARCHAR(255), polskie_slowa TEXT)"  # noqa: E501
            )
            file_path = Path("app/load_data/dictionaries") / filename
            with file_path.open(mode="r", encoding="utf-8") as file:
                for line in file:
                    elf_word, polish_word = line.strip().split(" - ", 1)
                    sql = f"INSERT INTO {tablename} (tlumaczenie, polskie_slowa) VALUES (%s, %s)"  # noqa: S608, E501
                    val = (elf_word, polish_word)
                    mycursor.execute(sql, val)

            mydb.commit()


if __name__ == "__main__":
    create_tables()
