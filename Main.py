'''
Created on Nov 18, 2015

@author: eltakwaa
'''
import Hangman

if __name__ == '__main__':
    pass

print("-----Hangman game-----")
print("This is a guessing game. You have to guess the letter of a word.")
print("If it's a correct guess then the letter will appear in its position.")
print("if no then you will lose one life")
print("***You have 6 available guesses***")
print("Press: ")
print("    (1) If you want to play.")
print("    (2) Exit.")

Press=input("Choice: ")

Hangman.CallHangmanGame(Press)