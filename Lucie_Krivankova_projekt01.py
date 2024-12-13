"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lucie Křivánková
email: luciekrivankova.10@gmail.com
discord: .torali
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = [
    {"username": "bob", "password": "123"},
    {"username": "ann", "password": "pass123"},
    {"username": "mike", "password": "password123"},
    {"username": "liz", "password": "pass123"}
        ]

line = "-" * 40

categories = {
    "titlecase": [],
    "uppercase": [],
    "lowercase": [],
    "numeric": [],
    "sum_numeric": [],
    "letter_counts": {}
            }


username_input = input("username: ")
password_input = input("password: ")
number_input = input("Enter a number between 1 and 3: ")

try:
    number_int = int(number_input)

    if 1 <= number_int <= 3:
        select_text = TEXTS[number_int - 1]
        words = (select_text.replace(",","").replace(".","")).split()
 
        for user in users:
            if user["username"] == username_input and user["password"] == password_input:
          
                for word in words:
                    if word[0].isupper():
                        categories["titlecase"].append(word)

                    if word.isalpha() and word.isupper():
                        categories["uppercase"].append(word)

                    if word.islower():
                        categories["lowercase"].append(word)

                    if word.isnumeric():
                        categories["numeric"].append(word)
                        categories["sum_numeric"].append(int(word))

                    word_length = len(word)
    
                    if word_length in categories["letter_counts"]:
                        categories["letter_counts"][word_length] += 1
                    else:
                        categories["letter_counts"][word_length] = 1
                
                    if (max_count := max(categories["letter_counts"].values()) + 1) % 2 == 0:
                        continue
                    else:
                        max_count += 1

                print(
                    "$ python projekt_1.py\n"
                    f"username: {username_input}\n"
                    f"password: {password_input}\n"
                    f"{line}\n"
                    f"Welcome to the app, {username_input}\n"
                    "We have 3 texts to be analyzed.\n"
                    f"{line}\n"
                    f"Enter a number btw. 1 and 3 to select: {number_int}\n"
                    f"{line}\n"
                    f"There are {len(words)} words in the selected text.\n"
                    f"There are {len(categories["titlecase"])} titlecase words.\n"
                    f"There are {len(categories["uppercase"])} uppercase words.\n"
                    f"There are {len(categories["lowercase"])} lowercase words.\n"
                    f"There are {len(categories["numeric"])} numeric strings.\n"
                    f"The sum of all the numbers {sum(categories["sum_numeric"])}\n"
                    f"{line}\n"
                    f"LEN|{"OCCURENCES".center(max_count)}|NR.\n"
                    f"{line}"
                    )

                for length, count in sorted(categories["letter_counts"].items()):
                    print(f"{str(length).rjust(3)}|{str("*" * count).ljust(max_count)}|{count}")

                break

        else:
            print(
                "$ python projekt_1.py\n"
                f"username: {username_input}\n"
                f"password: {password_input}\n"
                "Unregistered user, terminating the program.."
                )
    
    else:
        print(
            "$ python projekt_1.py\n"
            f"You wrote: {number_int}\n"
            "Invalid number for text analysis, terminating the program.."
            )

except ValueError:
    print(
        "$ python projekt_1.py\n"
        f"You wrote: {number_input}\n"
        "Invalid number for text analysis, terminating the program.."
        )
