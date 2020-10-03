
import random 

#make a list of words
words=['garden',
    'plant',
    'flower'
    'tree'
    'branch'
    'banana'
    'apple'
]
#select a random word from the list


while True:
    start=input("press enter/return to start guessing or enter Q to quit.")
    if start.lower()=='q':
        break

    secret_word=random.choice(words)
    bad_guessing=[]
    good_guessing=[]
    while(len(bad_guessing)<7) and (len(good_guessing)!=len(list(secret_word))):
        for letter in secret_word:
            if letter in good_guessing:
                print(letter,end='')
            else:
                print('_',end='')
        print(' ')
        print('strikes: {}/7'.format(len(bad_guessing)))
        print('')
        guess=input("Enter a letter: ").lower()
        if len(guess)!=1:
           print("you can only guess one letter: ")
           continue
        elif guess in good_guessing or guess in bad_guessing:
            print("You have already guess this letter")
        elif not guess.isalpha:
            print("You can only guess letters")
        if guess in secret_word:
            good_guessing.append(guess)
            if len(good_guessing)==len(list(secret_word)):
                print("you win! the word was  {}".format(secret_word))
                break
        else:
            bad_guessing.append(guess)
    else:
        print("you loose! the word was  {}".format(secret_word))



    