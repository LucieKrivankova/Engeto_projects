"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lucie Křivánková
email: luciekrivankova.10@gmail.com
discord: .torali
"""
import random

def cows_and_bulls(list1, list2):
    """
    Najde stejné číslice v obou listech (cows) nebo stejné číslice na stejné pozici (bulls).
    Zároveň rozlišuje množné a jednotné tvary ve výsledném textu.
    """  
    bulls = [list1[i] for i in range(len(list1)) if list1[i] == list2[i]]
    cows = list((set(list1) & set(list2)) - set(bulls))

    bull_text = "bull" if len(bulls) == 1 else "bulls"
    cow_text = "cow" if len(cows) == 1 else "cows"

    print(f"{bull_text} {len(bulls)}, {cow_text} {len(cows)}")


guess = 0
line = "-" * 47

print(
    "Hi there!\n"
    f"{line}\n"
    "I've generated a random 4 digit number for you.\n"
    "Let's play a bulls and cows game.\n"
    f"{line}\n"
    "Enter number:"
    )

ran_number = random.sample(range(1, 10), 1) + random.sample(range(0, 10), 3)
number_int = []

while number_int != ran_number:
    try:
        number_input = input("Enter number: ")

        if len(number_input) != 4 or (len(set(number_input)) != len(number_input)):
            print(f"{line}\nPlease, enter a uniqe four digit number.")
            continue

        number_int = [int(x) for x in number_input]
        
        print(f"{line}\n>>> {number_input}")
        cows_and_bulls(number_int, ran_number)
        guess += 1


    except ValueError:
        print(f"{line}\nPlease, enter a number.")
        continue


guess += 1
print(
    f"{line}\n"
    f">>> {number_input}\n"
    "Correct, you've guessed the right number\n"
    f"in {guess} guesses!\n"
    f"{line}\n"
    "That's amazing!"
    )
