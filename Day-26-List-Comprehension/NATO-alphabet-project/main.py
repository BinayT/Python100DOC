import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
letter_code_dict = {row.letter: row.code for (index, row) in data.iterrows()}

game_on = True
while game_on:
    name = input("Write your name to convert into Nato-Alphabet.. ").upper()
    name_to_list = [name[i] for i in range(len(name))]
    name_in_nato = [letter_code_dict[name] for name in name_to_list]
    print(name_in_nato)