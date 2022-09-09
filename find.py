import random

#random words
rand_word = ["exhibition", "chocolate", "oil", "basin", "elbow", "dignity", "sow", "action", "producer", "reason", "identification", "brother", "pie", "raid", "figure", "joy", "flatware", "post", "automatic", "pocket", "fragment", "apparatus", "executive", "endorse", "deep", "pour", "case", "zone", "length", "root"]

#hints for words
hint = ["a display or demonstration of a particular skill.", "a sweet treat that originates from a seed.", "blank doesn't mix with water.", "British word for sink.", "where is your funny bone?", "a sense of pride in oneself; self-respect.", "plant the seeds of (a plant or crop)", "the process of doing something.", "oversees the creation of films.", "a cause, explanation, or justification for an action or event.", "a driver's license is an example of blank.", "a man or boy in relation to other sons and daughters of his parents.", "a cherry blank.", "a sudden attack.", "kids like to play with an action blank.", "synonym for happy.", "another word for utensils.", "something (such as a message) that is published online.", "working by itself with little or no direct human control.", "I often carry my phone in my blank.", "a small part of something.", "a complex structure within an organization or system.", "the person or branch of a government responsible for putting policies or laws into effect.", "declare one's public approval or support of.", "this water is way too blank!", "when I am thirsty I am going to blank a drink.", "an instance of a disease or problem.", "an area or stretch of land having a particular charactearistic, purpose, or use, or subject to particular restrictions.", "the measurement of something from end to end.", "the part of the plant attached to the ground."]

#congratulation messages
rand_congrats = ["You got it!", "Congrats!", "You guessed the word!", "Niceeeeeee!", "You guessed correctly!"]

#sorry messages
rand_sorry = ["Sorry, try again.", ":( You didn't get it, try again.", "Play again!", "You'll get it next time!", "Aww man, try again."]


#introduction
print("Hello! Welcome to Guess the Word! The purpose of this game will be to guess different letters to try and figure out a certain word. You will have as many attempts as how long the word is + 2 additonal. I will provide you with a hint to get started, good luck!!")


#randomly selects a word and the accompanying hint
choice = random.randint(0, 29)
word = rand_word[choice]
print(hint[choice])

#randomly selects a congratulation message and a sorry message to be printed if required
message = random.randint(0, 4)
congrats = rand_congrats[message]
sorry = rand_sorry[message]


#creates a list with dashes in place for each character of the word
hidden = []

for x in word:
    hidden.append("-")

print(hidden)


#sets the amount of the attempts to the length of the word + 2
attempts = ((len(word)) + 2)
print("You will have " + str(attempts) + " attempts.")

        
#runs a loop as long as the guessed word is not equal to the word and the attempts are not eqaul to 0
while hidden != list(word) and attempts != 0:
    guess = input("Guess a letter:")

    print("You have " + str(attempts) + " attempts remaining.")

    #replaces letter/s in the hidden word if correct
    for i in range(len(word)):
        if guess == word[i]:
            hidden[i] = guess
            print(hidden)

    #prints an error message if the entered guess is nan or not a single character
    if not guess.isalpha() or len(guess) > 1:
        print("Please enter a single letter only!")
        attempts += 1

    attempts -= 1

    #breaks and prints congratulation message if the hidden word is equal to the word
    if hidden == list(word):
        print(congrats)
        print("The word was: " + word)
        break

    #prints sorry message if the attempts are equal to 0 and the hidden word is not equal to the word
    if attempts == 0 and hidden != list(word):
        print(sorry)
        print("The word was: " + word)
        

    
