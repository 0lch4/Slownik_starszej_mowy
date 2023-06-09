from . import create, loading

pairs = []
dictionary = {}

if __name__ =="__main__":
    data = create.import_data()
    create.tuples(data, pairs, dictionary)
    create.make_files(dictionary, "dictionaries")
    loading.create_tables()
