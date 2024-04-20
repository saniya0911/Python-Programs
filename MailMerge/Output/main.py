PLACEHOLDER = "[name]"


with open("./myprog/Projects/MailMerge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  #convert each line into a list

with open("./myprog/Projects/MailMerge/Input/Letters/starting_letter.txt") as letters_file:
    letter = letters_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./myprog/Projects/MailMerge/Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as mail:
            mail.write(new_letter)  