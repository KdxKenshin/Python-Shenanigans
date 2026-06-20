# Simple Quiz Game that asks the user 5 questions and keeps track of their score. It does this by using if statements to check if the user's answer is correct and then adds 1 to their score if it is. At the end, it prints out how many questions they got correct and their percentage score.
print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does NBA stand for? ")
if answer.lower() == "national basketball association":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")    
print("You got " + str((score/5) * 100) + "%.")       