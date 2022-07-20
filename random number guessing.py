import random

under_number=input("Enter a Number : ")

if under_number.isdigit():
    under_number=int(under_number)

    if under_number <=0:
        print("type a numver that is greater than 0")
        quit()
else:
    print("type a number next time!...")
    quit()

generate_random_no = random.randint(0,under_number)

guess_no = 0

while True:
    guess_no +=1
    input_guess=input("Guess the number : ")

    if input_guess.isdigit:
        input_guess=int(input_guess)
    else:
        print("please type number next time")
        continue
    if input_guess == generate_random_no:
        print("you got it right!...")
        break
    elif generate_random_no < int(input_guess):
        print("you have guessed num above the random number ")
    else:
        print("you have selected number below the random number")
        

print("you have guessed correctly in " +str(guess_no) + " guesses")
