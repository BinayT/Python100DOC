import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
letter_code_dict = {row.letter: row.code for (index, row) in data.iterrows()}

game_on = True
while game_on:
    name = input("Write your name to convert into Nato-Alphabet...\n").upper()
    name_to_list = [name[i] for i in range(len(name))]
    name_in_nato = []
    for x in name_to_list:
        try:
            name_in_nato.append(letter_code_dict[x])
        except KeyError:
            pass
    print(name_in_nato)