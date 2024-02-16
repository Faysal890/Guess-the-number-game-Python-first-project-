import random

target = random.randint(1,100)
attempt = 10
print("You have {} attempt, For every failed attempt your score will be decreased by one. Every attempt equal to 1 point".format(attempt))
print("---To quit game press q---");
while attempt>0:
    num = input("Enter your number or to exit enter e : ")
    if num=='e':
        break
    else:
        num = int(num)
    if num == target:
        print("Congratulation, Your score is {}".format(attempt))
        break
    elif num<target:
        print("Your guess number is smaller than target")
    else:
        print("Your guess number is greater than target")
    attempt = attempt-1

if attempt == 0:
    print("---Opps! you loss the game---")