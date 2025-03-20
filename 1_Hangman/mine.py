from hangman_words import words
from hangman_ASCll import hangman
import random

print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  \n """)

random_word = random.choice(words)
under_score = []
wrong_words = []
numbers = 6
condition = True

for letter in random_word:
    under_score.append(" _ ")


print(random_word)
while condition:

    matched = False
    user_answer = input("What is your guess?\n").lower()

    for possession in range(len(random_word)):
        letter = random_word[possession]

        if letter == user_answer :
            under_score[possession] = letter
            matched = True

    if matched:
        print(under_score)

    if user_answer not in random_word :

        if numbers == 0 :
            print("you are lose!")
            condition = False

        if user_answer not in wrong_words :
            numbers -= 1
            wrong_words.append(user_answer)
            print(f"{hangman[len(wrong_words) * -1]}\n")

        print(f"'{user_answer}' does not exist!\n")
    if " _ " not in under_score:
        print("you won")
        condition = False
