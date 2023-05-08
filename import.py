import requests
from bs4 import BeautifulSoup


class Get_data:
    def __init__(self,critery,selector=None):
        self.response = 'https://wiedzmin.fandom.com/wiki/S%C5%82ownik_starszej_mowy'
        self.critery = critery
        self.selector = selector
        self.soup = None
        
    def take(self):
        self.response = requests.get(self.response)
        self.soup = BeautifulSoup(self.response.text, 'lxml')
        self.critery= self.soup.select(self.critery)
            
    def show(self):
        for i in self.critery:
            print(i)
            
    def find(self):
        if self.selector is None:
            pass
        else:
            for i in self.soup.find_all(self.selector):
                print(i)
                

primary_key = Get_data('.mw-headline')

primary_key.take()
primary_key.show()

literki = Get_data('ul')

literki.take()
literki.find()


        