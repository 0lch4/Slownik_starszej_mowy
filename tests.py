import pytest
import os
from mydb import conn
from fastapi.testclient import TestClient

#testy sprawdzajace poprawnosc dzialania

mydb = conn()

import plik
def test_tuples():
    data = '''Aecáemm - podążać
        Aedd - okruch
        Deien - służyć
        Waen - chcieć'''
        
    data = data.split('\n')
    dictionary = {}
    pairs = []

    expected_pairs = [('Aecáemm', 'podążać'), ('Aedd', 'okruch'), ('Deien', 'służyć'), ('Waen', 'chcieć')]
    expected_dict = {'p': [('Aecáemm', 'podążać')],'o': [('Aedd', 'okruch')], 's':[('Deien', 'służyć')], 'c': [('Waen', 'chcieć')]}

    plik.tuples(data, pairs, dictionary)

    assert pairs == expected_pairs
    assert dictionary == expected_dict
    
    
def test_make_files():
    dictionary = {'p': [('Aecáemm', 'podążać')],'o': [('Aedd', 'okruch')], 's':[('Deien', 'służyć')], 'c': [('Waen', 'chcieć')]}

    
    with open('tests_files/makefile/A.txt','w',encoding="utf-8") as f:
        f.write('Aecáemm - podążać\nAedd - okruch')
    with open('tests_files/makefile/D.txt','w',encoding="utf-8") as f:
        f.write('Deien - służyć')
    with open('tests_files/makefile/W.txt','w',encoding="utf-8") as f:
        f.write('Waen - chcieć')
        
    plik.make_files(dictionary,'tests_files/makefile')
    
    with open('tests_files/makefile/A.txt','r',encoding="utf-8") as f:
        assert f.read() == 'Aecáemm - podążać\nAedd - okruch'
    with open('tests_files/makefile/D.txt','r',encoding="utf-8") as f:
        assert f.read() == 'Deien - służyć'
    with open('tests_files/makefile/W.txt','r',encoding="utf-8") as f:
        assert f.read() == 'Waen - chcieć'
        
        
import loading

def test_create_tables2():
    for filename in os.listdir("tests_files"):
        if filename.endswith(".txt"):
            tablename = os.path.splitext(filename)[0]

            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE {} (slowo VARCHAR(255), tlumaczenie TEXT)".format(tablename))

            with loading.open_file(os.path.join("tests_files", filename)) as file:
                for line in file:
                    slowo, tlumaczenie = line.strip().split(' - ', 1)
                    val = (slowo, tlumaczenie)
    
    assert tablename == 'test1'
    assert val == ('is this', 'work')
    mycursor.execute("DROP TABLE IF EXISTS test1")
    


from main import app

client = TestClient(app)

def test_submit_form():
    response = client.post("/submit", data={"words": "wilk"})
    assert response.status_code == 200
    assert "Bleidd" in response.text