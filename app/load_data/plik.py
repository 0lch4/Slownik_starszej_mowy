pairs = []
dictionary = {}


def import_data():
    with open("data.txt", "r", encoding="utf-8") as f:
        data = f.read()
    data = data.split("\n")
    return data


#parses data.txt and creates a file starting with the
#first letter of the word with word - translation pairs'''
def tuples(data, pairs, dictionary):
    for line in data:
        sides = line.split("-")
        elf_words = sides[0].strip()
        polish_words = sides[1].strip()
        del_comma = polish_words.replace(",", " -")
        all_words = del_comma.split("-")
        for word in all_words:
            word = word.strip()
            tupl = (elf_words, word)
            first_letter = word[0]
            if first_letter in dictionary:
                dictionary[first_letter].append(tupl)
            else:
                dictionary[first_letter] = [tupl]
            pairs.append(tupl)


def make_files(dictionary, dirr):
    for letter, pair in dictionary.items():
        with open(f"{dirr}/{letter}.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(f"{word[0]} - {word[1]}" for word in pair))


if __name__ == "__main__":
    data = import_data()
    tuples(data, pairs, dictionary)
    make_files(dictionary, "dictonaries")
