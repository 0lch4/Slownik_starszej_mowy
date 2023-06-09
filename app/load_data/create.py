from pathlib import Path

pairs = []
dictionary = {}


def import_data() -> list:
    file_path = Path("app/load_data/data.txt")
    with file_path.open(mode="r", encoding="utf-8") as file:
        data = file.read()
    data = data.split("\n")
    return data


# parses data.txt and creates a file starting with the
# first letter of the word with word - translation pairs
def tuples(data: list, pairs: list, dictionary: dict) -> None:
    for line in data:
        sides = line.split("-")
        elf_words = sides[0].strip()
        polish_words = sides[1].strip()
        del_comma = polish_words.replace(",", " -")
        all_words = del_comma.split("-")
        for word in all_words:
            word = word.strip()  # noqa: PLW2901
            tupl = (elf_words, word)
            first_letter = word[0]
            if first_letter in dictionary:
                dictionary[first_letter].append(tupl)
            else:
                dictionary[first_letter] = [tupl]
            pairs.append(tupl)


def make_files(dictionary: dict, dirr: str) -> None:
    path = Path(f"app/load_data/{dirr}")
    for letter, pair in dictionary.items():
        file_path = path / f"{letter}.txt"
        with file_path.open(mode="a", encoding="utf-8") as file:
            file.write("\n".join(f"{word[0]} - {word[1]}" for word in pair))


if __name__ == "__main__":
    data = import_data()
    tuples(data, pairs, dictionary)
    make_files(dictionary, "dictionaries")
