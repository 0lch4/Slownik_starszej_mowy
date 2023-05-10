import pytest
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv('host'),
    user=os.getenv('user'),
    password=os.getenv('password'),
    database=os.getenv('database'),
    charset='utf8mb4'
)

import plik

def test_tuples():
    dane = '''Aecáemm - podążać
        Aedd - okruch
        Deien - służyć
        Waen - chcieć'''
        
    
    dane = dane.split('\n')
    slowniczek = {}
    slownik = []

    expected_slownik = [('Aecáemm', 'podążać'), ('Aedd', 'okruch'), ('Deien', 'służyć'), ('Waen', 'chcieć')]
    expected_slowniczek = {'A': [('Aecáemm', 'podążać'),('Aedd', 'okruch')], 'D':[('Deien', 'służyć')], 'W': [('Waen', 'chcieć')]}

    plik.tuples(dane, slownik, slowniczek)

    assert slownik == expected_slownik
    assert slowniczek == expected_slowniczek
    
    
def test_make_files():
    slowniczek = {'A': [('Aecáemm', 'podążać'),('Aedd', 'okruch')], 'D':[('Deien', 'służyć')], 'W': [('Waen', 'chcieć')]}
    
    with open('tests/makefile/A.txt','w') as f:
        f.write('Aecáemm - podążać\nAedd - okruch')
    with open('tests/makefile/D.txt','w') as f:
        f.write('Deien - służyć')
    with open('tests/makefile/W.txt','w') as f:
        f.write('Waen - chcieć')
        
    plik.make_files(slowniczek)
    
    with open('tests/makefile/A.txt','r') as f:
        assert f.read() == 'Aecáemm - podążać\nAedd - okruch'
    with open('tests/makefile/D.txt','r') as f:
        assert f.read() == 'Deien - służyć'
    with open('tests/makefile/W.txt','r') as f:
        assert f.read() == 'Waen - chcieć'
        
        
import ladowanie

def test_create_tables2():
    
    for filename in os.listdir("tests"):
        if filename.endswith(".txt"):
            tablename = os.path.splitext(filename)[0]

            mycursor = mydb.cursor()
            mycursor.execute("DROP TABLE test1")
            mycursor.execute("CREATE TABLE {} (slowo VARCHAR(255), tlumaczenie TEXT)".format(tablename))

            with ladowanie.open_file(os.path.join("tests", filename)) as file:
                for line in file:
                    slowo, tlumaczenie = line.strip().split(' - ', 1)
                    sql = "INSERT INTO {} (slowo, tlumaczenie) VALUES (%s, %s)".format(tablename)
                    val = (slowo, tlumaczenie)
    
    assert tablename == 'test1'
    assert val == ('is this', 'work')