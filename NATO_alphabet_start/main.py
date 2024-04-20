import pandas

data = pandas.read_csv("myprog/Projects/NATO_alphabet_start/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

def generate():
    word = input("Enter a word: ").upper()
    try:
        codewords = [phonetic_dict[letters] for letters in word]
    except KeyError as error_message:
        print("Sorry! Only the letters of the alphabet Please.")
        generate()
    else:
        print(codewords)

generate()