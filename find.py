import random

rand_word = ["exhibition", "chocolate", "oil", "basin", "elbow", "dignity", "sow", "action", "producer", "reason", "identification", "brother", "pie", "raid", "figure", "joy", "flatware", "post", "automatic", "pocket", "fragment", "apparatus", "executive", "endorse", "deep", "pour", "case", "zone", "length", "root"]

hint = ["a display or demonstration of a particular skill.", "a sweet treat that originates from a seed.", "blank doesn't mix with water.", "British word for sink.", "where is your funny bone?", "a sense of pride in oneself; self-respect.", "plant the seeds of (a plant or crop)", "the process of doing something.", "oversees the creation of films.", "a cause, explanation, or justification for an action or event.", "a driver's license is an example of blank.", "a man or boy in relation to other sons and daughters of his parents.", "a cherry blank.", "a sudden attack.", "kids like to play with an action blank.", "synonym for happy.", "another word for utensils.", "something (such as a message) that is published online.", "working by itself with little or no direct human control.", "I often carry my phone in my blank.", "a small part of something.", "a complex structure within an organization or system.", "the person or branch of a government responsible for putting policies or laws into effect.", "declare one's public approval or support of.", "this water is way too blank!", "when I am thirsty I am going to blank a drink.", "an instance of a disease or problem.", "an area or stretch of land having a particular characteristic, purpose, or use, or subject to particular restrictions.", "the measurement of something from end to end.", "the part of the plant attached to the ground."]

choice = random.randint(1, 30)
word = rand_word[choice]
print(hint[choice])

hidden = []

for x in word:
    hidden.append("-")

attempts = (len(word)) + 2
print("You have " + str(attempts) + " attempts.")

# for attempts in range(attempts + 1):


# print("Please enter only one character at a time.")
        
while hidden != list(word):
    guess = input("Enter a character:")

    for i in range(len(word)):
        if guess == word[i]:
            hidden[i] = guess
            print(hidden)

    

    
