import random
list_of_answers=['fashion','model','clothes','brand']

#pick randomly a word from the list to guess
random.shuffle(list_of_answers)

#split the word in to single characters in a list example: ['m','o','d','e','l']
answer=list(list_of_answers[0])

#create an empty list 
display=[]

display.extend(answer)
for i in range(len(display)):
    #display from ['m','o','d','e','l']->['-','-','-','-','-']
    display[i]='_' 
print(' '.join(display))   
print()

count=0

while count<len(answer):
    

    guess=input('Enter a letter: ').lower()
    print(count)
   
    for i in range(len(answer)):
        if answer[i]==guess:
            #display.append(guess)
            display[i]=guess
            count=count+1 

          
               

    print(' '.join(display))


  
    


