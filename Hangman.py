'''
Created on Nov 12, 2015

@author: Mika
'''
import random
import sys
import UpdateList
import DrawHangman

def CallHangmanGame(Press):
    if Press=='1':
        #Generate random number
        RandomIndexWord= random.uniform(0, 10)
        RandomIndexWord=int(RandomIndexWord)
    
        #Read specific line from file
        Word = open("Words.txt", "r").readlines()[RandomIndexWord]
    
        #print(Word)
    
        #Number of letters in a word and deduct 1 from it as it return extra number
        NunmberOfLettersInAWord= len(Word) - 1
        ListIncludeDashesAndLettersOfWord=[]
    
        #print(NunmberOfLettersInAWord)
        # -------------------------------- Printing dashes at the beginning ---------------------
    
        #check if the Word contain a space
    
        if (' ' in Word) == True:
            #Get index of space
            IndexOfSpace= Word.index(' ')
        
            #loop on number of letters in a word to detect if it includes a space
        
            j=0;
            while j<NunmberOfLettersInAWord:
                #If this index the one which includes the space in the word ... then print double space of the screen game
                if j==IndexOfSpace:
                
                    #print without new line for every space or dash
                    sys.stdout.write(' ')
                    ListIncludeDashesAndLettersOfWord.insert(j, ' ')
                
                else:
                    sys.stdout.write('_')
                    ListIncludeDashesAndLettersOfWord.insert(j, '_')
                
                j+=1
    
        else:
            i=0
            while i<NunmberOfLettersInAWord:
                sys.stdout.write('_')
                ListIncludeDashesAndLettersOfWord.insert(i, '_')
                
                i+=1
     
        #print(ListIncludeDashesAndLettersOfWord)       
        #-------------------------------------------------------------------------------------------
    
        print ()
        print ()
    
        #ListIncludeDashesAndLettersOfWord= [len(Word)]
        NumberOfGuesses=6
        UsedLetters=""
    
        while NumberOfGuesses>0:
            if '_' in ListIncludeDashesAndLettersOfWord:
                InputLetterFromUser= input("Your guess (Letters only): ")
            
                CheckAvailablityOfCharacter=ord(InputLetterFromUser)
                if (CheckAvailablityOfCharacter>= 97 and CheckAvailablityOfCharacter<=122) or (CheckAvailablityOfCharacter>=65 and CheckAvailablityOfCharacter<=90):
                    LetterExistInWord= Word.find(InputLetterFromUser)
                
                    #---------------  Check if letter Exist used before ----------------------    
                    if LetterExistInWord== -1:
                        BooleanLetterExistInWord= False
                    
                    else:
                        BooleanLetterExistInWord= True
            
                    #---------------  Check if letter is used before ----------------------    
                    if InputLetterFromUser in UsedLetters:
                        BooleanExistLetterInUsedLetterList = True
            
                    else:
                        BooleanExistLetterInUsedLetterList = False 
            
                    #-------------------------------------
        
                    # If the letter exist in the word    and   not existed in the used letters
                    if BooleanLetterExistInWord==True and BooleanExistLetterInUsedLetterList==False:
                        UsedLetters+=InputLetterFromUser+ ", "
                        print()
                        print("Used and missed letters/Digits: ", UsedLetters)
                        print("Chances remaining: ", NumberOfGuesses)
                        print("Word: ", UpdateList.UpdateListThatIncludeDashedAndLetterOfWord(InputLetterFromUser, Word, ListIncludeDashesAndLettersOfWord))
        
                    # If the letter not exist in the word    and   not existed in the used letters    
                    elif BooleanLetterExistInWord==False and BooleanExistLetterInUsedLetterList==False:
                        NumberOfGuesses-=1
                        print()
                        print("This character is not valid in the word.")
                        UsedLetters+=InputLetterFromUser+ ", "
                        print("Used and missed letters/Digits: ", UsedLetters)
                        DrawHangman.KMDrawHangman(NumberOfGuesses)
                        print("Chances remaining: ", NumberOfGuesses)
                        print("Word: ", "".join(ListIncludeDashesAndLettersOfWord))
            
                    else:
                        print()
                        print("You have already tried this letter or digit.")
                        print("Guess again")
        
                else:
                    print()
                    print("Not a valid character. Please enter a letter")
         
            else:
                print()
                print("*********************")
                print("*Congratulations ^_^*")
                print("*You won.           *")
                print("*********************")
                
                print("Press: ")
                print("    (1) If you want to play again.")
                print("    (2) Exit.")
                Press=input("Choice is: ")
                
                CallHangmanGame(Press)
                
                break
     
        if NumberOfGuesses<=0 :
            print()
            print("*********************")
            print("*Ewwww... Sorry :(  *")
            print("*You lose.          *")
            print("*********************")
            
            DrawHangman.KMDrawHangman(NumberOfGuesses)
                
            print("Press: ")
            print("    (1) If you want to play again.")
            print("    (2) Exit.")
            Press=input("Choice is: ") 
            
            CallHangmanGame(Press)
            
    elif Press=='2':
        print ("Good bye... ")
        exit()
    
    else:
        print("Just press 1 or 2, there are no other choices :D")
        print("Press: ")
        print("    (1) If you want to play again.")
        print("    (2) Exit.")
        Press=input("Choice is: ") 
            
        CallHangmanGame(Press)

    