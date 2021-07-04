import random


def RPS(number): 
    random_number = random.randrange(1,5)
    if(number == random_number):
        print("it's a draw!")

    if (random_number == 1):
        if(number == 2):
            print("you lose, I chose Paper")
        if (number == 3):
            print("you win, I chose Scissors")
        if (number == 4):
            print("you win, I chose Lizard")
        if (number == 5):
            print("you lose, I chose Spock")

    elif (random_number == 2):
        if(number == 1):
            print("you win, I chose Rock")
        if (number == 3):
            print("you lose, I chose Scissors")
        if (number == 4):
            print("you lose, I chose Lizard")
        if (number == 5):
            print("you win, I chose Spock")

    elif (random_number == 3):
        if(number == 2):
            print("you win, I chose Paper")
        if (number == 3):
            print("you lose, I chose Rock")
        if (number == 4):
            print("you win, I chose Lizard")
        if (number == 5):
            print("you lose, I chose Spock")

    elif (random_number == 4):
        if(number == 2):
            print("you win, I chose Paper")
        if (number == 3):
            print("you lose, I chose Scissors")
        if (number == 1):
            print("you lose, I chose Rock")
        if (number == 5):
            print("you win, I chose Spock")

    elif (random_number == 5):
        if(number == 2):
            print("you win, I chose Paper")
        if (number == 3):
            print("you lose, I chose Scissors")
        if (number == 4):
            print("you win, I chose Lizard")
        if (number == 1):
            print("you lose, I chose Rock")

while True:
    print('1. Rock\n2. Paper\n3. Scissors\n4. Lizard\n5. Spock')
    rps = input()
    print(rps)
    RPS(int(rps))