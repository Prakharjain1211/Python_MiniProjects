# ************ Quiz Game ************

print("Welcome to my computer quiz!")

playing = input("Do you want to play? : ")
playing = playing.lower()

if playing !="yes":
    quit()

print("Okay! Let's play :)")

count = 0
answer = input("What does cpu stands for? ")
answer = answer.lower()

if answer == 'central processing unit':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')


answer = input("What does gpu stands for? ")
answer = answer.lower()
if answer == 'graphics processing unit':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')


answer = input("What does ram stands for? ")
answer = answer.lower()
if answer == 'random access memory':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')


answer = input("What does psu stands for? ")
answer = answer.lower()
if answer == 'power supply':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')
    
answer = input("What does rom stands for? ")
answer = answer.lower()
if answer == 'read only memory':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')
    
print()
print("Your score:",count,"/5")
print("you got " + str((count/5)*100) +"%")