'''
Created on Nov 17, 2015

@author: Mika
'''

def UpdateListThatIncludeDashedAndLetterOfWord(InputLetterFromUser, Word, ListIncludeDashesAndLettersOfWord):
        i = 0
        while i < len(Word):
            if InputLetterFromUser == Word[i]:
                ListIncludeDashesAndLettersOfWord[i] = InputLetterFromUser
                i+=1
            else:
                i+=1

        return "".join(ListIncludeDashesAndLettersOfWord)
