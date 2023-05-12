pairs = []
dictionary = {}
#importuje dane z pliku data.txt zawierajacego znane slowa 
def import_data():
    with open('data.txt','r',encoding='utf-8') as f:
        data = f.read()
    data = data.split('\n')
    return data

#rodziela wszystko tak abypowstaly pary: slowo-tlumaczenie i byly przypisane do pierwszej litery polskiego slowa
def tuples(data,pairs,dictionary):
    for line in data:
        #podzial na czesc polska i elfia
        sides = line.split('-')
        elf_words = sides[0].strip()
        polish_words = sides[1].strip()
        '''zamiana , na - i ponowe rozdzielenie dopiero po rozdzieleniu na polską i elfią strone
        aby wszystkie slowa zostaly poprawnie przypisane'''
        del_comma = polish_words.replace(',',' -')
        all_words = del_comma.split('-')
        for word in all_words:
            #usuwanie zbednych spacji
            word = word.strip()
            #para tlumaczen
            tupl = (elf_words,word)
            #wyznaczenie pierwszej litery i przypisanie wartosci
            first_letter = word[0]
            if first_letter in dictionary:
                dictionary[first_letter].append(tupl)
            else:
                dictionary[first_letter] = [tupl]            
            pairs.append(tupl)

#tworzenie plikow o nazwie pierwszej litery polskiego slowa, ktorych zawartosc to slowo - tlumaczenie        
def make_files(dictionary,dirr):
    for letter, pair in dictionary.items():
        with open(f"{dirr}/{letter}.txt", "a", encoding="utf-8") as f:
            f.write('\n'.join([f"{word[0]} - {word[1]}" for word in pair]))
            
#aby ta czesc nie wykonywala sie podczas importu                                    
if __name__ == '__main__':
    data = import_data()
    tuples(data,pairs,dictionary)
    make_files(dictionary,'dictonaries')
