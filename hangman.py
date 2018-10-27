import random

def play(word):
    entered = []
    guesses = ''
    count = -1
    turns = 6
    while turns > 0:
        count += 1         
        failed = 0             
        for char in word:      
            if char in guesses:
                print(char,end=" ")    
            else:
                print("_",end=" ")
                failed += 1    
        if failed == 0:        
            print(" (You got it after picking",count,"letters)")  
            break              
        print("(",turns,"error-attempts left )") 

        print()
        guess = input("Guess a letter: ")
        guesses += guess                    

        if guess in entered:
            print("You have already entered ",guess)
            count -= 1
            continue
        else:
            entered.append(guess)

        if guess not in word:  
            turns -= 1
            print("There is no",guess)  
     
            if turns == 0:
                print ("The secret word was",word,". Good luck next time.")

def main():
    try:
        print("Welcome to Hangman!")
        wl_file = open("wordlist.txt","r")
        word_list = wl_file.read().replace("\n",",").split(",")
        random_word = random.choice(word_list)
        play(random_word)
    except:
        print("wordlist.txt not found! please create wordlist.txt with comma separated words")

if __name__ == '__main__':
    main()

