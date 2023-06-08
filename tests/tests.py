import os
from fastapi.testclient import TestClient
from pathlib import Path
from app.connection.mydb import conn
from app.main import app
from app.load_data import create


mydb = conn()


def test_tuples() -> None:
    data = """Aecáemm - podążać
        Aedd - okruch
        Deien - służyć
        Waen - chcieć"""

    data = data.split("\n")
    dictionary = {}
    pairs = []

    expected_pairs = [
        ("Aecáemm", "podążać"),
        ("Aedd", "okruch"),
        ("Deien", "służyć"),
        ("Waen", "chcieć"),
    ]
    expected_dict = {
        "p": [("Aecáemm", "podążać")],
        "o": [("Aedd", "okruch")],
        "s": [("Deien", "służyć")],
        "c": [("Waen", "chcieć")],
    }

    create.tuples(data, pairs, dictionary)

    assert pairs == expected_pairs
    assert dictionary == expected_dict


def test_make_files() -> None:
    dictionary = {
        "p": [("Aecáemm", "podążać")],
        "o": [("Aedd", "okruch")],
        "s": [("Deien", "służyć")],
        "c": [("Waen", "chcieć")],
    }

    file_path = Path("tests/tests_files/makefile/A.txt")
    with file_path.open(mode="w", encoding="utf-8") as file:
        file.write("Aecáemm - podążać\nAedd - okruch")

    file_path = Path("tests/tests_files/makefile/D.txt")
    with file_path.open(mode="w", encoding="utf-8") as file:
        file.write("Deien - służyć")

    file_path = Path("tests/tests_files/makefile/W.txt")
    with file_path.open(mode="w", encoding="utf-8") as file:
        file.write("Waen - chcieć")

    create.make_files(dictionary, "tests/tests_files/makefile")

    file_path = Path("tests/tests_files/makefile/A.txt")
    with file_path.open(mode="r", encoding="utf-8") as file:
        assert file.read() == "Aecáemm - podążać\nAedd - okruch"

    file_path = Path("tests/tests_files/makefile/D.txt")
    with file_path.open(mode="r", encoding="utf-8") as file:
        assert file.read() == "Deien - służyć"

    file_path = Path("tests/tests_files/makefile/W.txt")
    with file_path.open(mode="r", encoding="utf-8") as file:
        assert file.read() == "Waen - chcieć"


def test_create_tables2() -> None:
    for filename in os.listdir("tests/tests_files"):
        if filename.endswith(".txt"):
            tablename = Path.suffix(filename)[0]
            mycursor = mydb.cursor()
            mycursor.execute(
                f"CREATE TABLE {tablename} (slowo VARCHAR(255), tlumaczenie TEXT)"
            )

            file_path = Path("tests_files") / filename
            with file_path.open(mode="r") as file:
                for line in file:
                    slowo, tlumaczenie = line.strip().split(" - ", 1)
                    val = (slowo, tlumaczenie)

    assert tablename == "test1"
    assert val == ("is this", "work")
    mycursor.execute("DROP TABLE IF EXISTS test1")


client = TestClient(app)


def test_submit_form() -> None:
    response = client.post("/submit", data={"words": "wilk"})
    assert response.status_code == 200
    assert "Bleidd" in response.text
