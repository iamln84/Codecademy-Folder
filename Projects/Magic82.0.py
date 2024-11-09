import random

# Name of player asking the question
player_name = "Wendy"

# Q&A variables
player_question = "Am I good at soccer?"
answer = ""

# Randomly generated value
random_number = random.randint(1, 10)

# Core logic of the program
if random_number == 1:
    answer = "Yes, definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Maybe so"
else:
    answer = "Error"

# If no name or question is implmented
if player_name == "":
    print("Question: " + player_question)
else:
    print(player_name + " asks: " + player_question)
if player_question == "":
    print("No question has been asked")
else:
    print("Magic 8-Ball's answer: " + answer)