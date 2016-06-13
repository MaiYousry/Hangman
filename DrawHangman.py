'''
Created on Nov 18, 2015

@author: eltakwaa
'''
def KMDrawHangman(NumberOfGuesses):
        
        if NumberOfGuesses == 5:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif NumberOfGuesses == 4:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
        elif NumberOfGuesses == 3:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif NumberOfGuesses == 2:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif NumberOfGuesses == 1:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|     /|\     ")
            print("|     /       ")
            print( "|            ")
        else:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|             ")
            print("You are dead!! ...")
            print("GAME OVE")