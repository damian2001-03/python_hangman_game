import sys
import random


print("Hello! Enter yours number of tries (max 5): ")
number_of_tries =int(input())

 
while number_of_tries>5 or number_of_tries<=0:
    print("You can have only max 5 tries, enter again: ")
    number_of_tries = int(input())
    

word = ["amazing", "colorful", "own", "angry", "serious", "rifle", "overwatch", "image"]
word = random.choice(word)

used_letters = []

user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    
    
    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Number of tries:", number_of_tries)
    print("Letters used:", used_letters)
    print()

###

for _ in word:
    user_word.append("_")

while True:
    letter = input("Enter a letter: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0 :
        print("There isn't this letter :/")
        number_of_tries-=1
        
        if number_of_tries == 0 :
            print("Game Over :(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter
        

        if "".join(user_word) == word:
            print("Congratulations,",word,"is this word!")
            sys.exit(0)


    show_state_of_game()