#Author: George Tzoumanekas
#Command Line Version of the popular New York Times Game Wordle in Python

import random
from urllib.request import urlopen
from colorama import Fore, Back, Style

#Finding a word and filtering it to be 5 letters
word_site = "http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
response = urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()
WORDS_5 = list(filter(lambda x: len(x) == 5, WORDS))
#this produces bytes and not strings so we'll convert it

list_of_words = []

#decoding to strings
for i in WORDS_5:
    list_of_words.append(i.decode("utf-8"))

#choose a random word from the list
randomword=(random.choice(list_of_words))

#if the user gives a word that's not 5 letters or that's not in the list it's not a vaid try
def isvalid(word):
    if (len(word) == 5 and word in list_of_words):
        return True
    else:
        return False

lis = list(randomword) #list of all the letters in the chosen word

tries = 6

while (tries > 0):
    inputword = input("Make a guess:\n")    
    c = 0 #counter to keep the row of the letter
    
    lst1 = [] # char
    lst2 = [] # 0:doesn't exist, 1:exists but wrong position, 2: right position

    if (isvalid(inputword) == False):
        print("Invalid word")
        continue

    for i in list(inputword):
        var1 = False #exist
        var2 = False #position

        for j in range (0,len(lis)):
            if (i == lis[j]):
                var1 = True
                if (c == j):
                    var2 = True #right position

        if (var2): #right position
            lst1.append(i)
            lst2.append(2)
        elif (var2 == False and var1 == True): #right letter
            lst1.append(i)
            lst2.append(1)
        else: #wrong letter
            lst1.append(i)
            lst2.append(0)

        c+=1

    # you found the word
    if (inputword == randomword):
        for i in range (5):
            print(Fore.GREEN + lst1[i], end =" ")
        print('\n')
        print(Fore.WHITE + "Congrats!!!")
        break

    # this prints the letters (green for the right ones and yellow for the ones that exist in another position)
    for i in range (5):
        if (lst2[i] == 0):
            print(Fore.WHITE + lst1[i], end =" ")
        elif (lst2[i] == 1):
            print(Fore.YELLOW + lst1[i], end =" ")
        else:
            print(Fore.GREEN + lst1[i], end =" ")

    print(Fore.WHITE + "\n")
    tries-=1

# maximum number of tries means you didn't find the word
if (tries == 0):
    print("I'm sorry, you lost. The word is", randomword)
