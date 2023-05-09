import requests
from bs4 import BeautifulSoup

letters=[]

class Get_data:
    def __init__(self,lista,critery,selector=None):
        self.response = 'https://wiedzmin.fandom.com/wiki/S%C5%82ownik_starszej_mowy'
        self.critery = critery
        self.selector = selector
        self.soup = None
        self.lista = lista
        
    def take(self):
        self.response = requests.get(self.response)
        self.soup = BeautifulSoup(self.response.text, 'lxml')
        self.critery= self.soup.select(self.critery)
            
    def show(self):
        for i in self.critery:
            self.lista.append(i.text)
            
    def find(self):
        if self.selector is None:
            pass
        else:
            for i in self.soup.find_all(self.selector):
                self.lista.append(i.text)
                
    def only_letters(self):
        self.lista = [i for i in self.lista if len(i)<=1]
        self.lista = set(self.lista)
        alphabet = sorted(self.lista)
        return alphabet



primary_key = Get_data(letters,'.mw-headline','h3')
primary_key.take()
primary_key.find()
letters = primary_key.only_letters()



