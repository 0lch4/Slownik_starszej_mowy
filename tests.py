import pytest

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
    
    with open('A.txt','w') as f:
        f.write('Aecáemm - podążać\nAedd - okruch')
    with open('D.txt','w') as f:
        f.write('Deien - służyć')
    with open('W.txt','w') as f:
        f.write('Waen - chcieć')
        
    plik.make_files(slowniczek)
    
    with open('A.txt','r') as f:
        assert f.read() == 'Aecáemm - podążać\nAedd - okruch'
    with open('D.txt','r') as f:
        assert f.read() == 'Deien - służyć'
    with open('W.txt','r') as f:
        assert f.read() == 'Waen - chcieć'
        