import random

animals = ["Tiger", "Cow", "Cat", "Dog", "Eagle", "Elephant", "Fish", "Shark", "Dolphin", "Monkey"]

computer_choice = random.choice(animals)

clues = [1, 2, 3, 4, 5]
choice = 1
while(choice):
    if(computer_choice == "Tiger"):
        print("Clue 1 -> I have four legs")
        guess = input("enter your guess: ")
        if(guess == computer_choice):
            print(f"That's right its a {computer_choice}")
            choice = 0
        else:
            print("Clue 2: I have orange body with black stripes")
            guess = input("enter your guess: ")
            if(guess == computer_choice):
                print(f"That's right its a {computer_choice}")
                choice = 0
            else:
                print("Clue 3: Looks like a big cat")
                guess = input("enter your guess: ")
                if(guess == computer_choice):
                    print(f"That's right its a {computer_choice}")
                    choice = 0
                else:
                    print("Clue 4: Sharp teeth and claws")
                    guess = input("enter your guess: ")
                    if(guess == computer_choice):
                        print(f"That's right its a {computer_choice}")
                        choice = 0
                    else:
                        print("Clue 5: Lives in forests and jungles")
                        guess = input("enter your guess: ")
                        if(guess == computer_choice):
                            print(f"That's right its a {computer_choice}")
                            choice = 0
                        else:
                            print(f"sorry you are out of turns!\n")
                            print("You lose")
                            print(f"The correct answer is {computer_choice}")
                            choice = 0


    if(computer_choice == "Cow"):
        print("Clue 1 -> Big farm animal.")
        guess = input("enter your guess: ")
        if(guess == computer_choice):
            print(f"That's right its a {computer_choice}")
            choice = 0
        else:
            print("Clue 2: Usually white, brown, or black")
            guess = input("enter your guess: ")
            if(guess == computer_choice):
                print(f"That's right its a {computer_choice}")
                choice = 0
            else:
                print("Clue 3: Gives us milk")
                guess = input("enter your guess: ")
                if(guess == computer_choice):
                    print(f"That's right its a {computer_choice}")
                    choice = 0
                else:
                    print("Clue 4: Eats grass.")
                    guess = input("enter your guess: ")
                    if(guess == computer_choice):
                        print(f"That's right its a {computer_choice}")
                        choice = 0
                    else:
                        print("Clue 5: Says 'Moo!'")
                        guess = input("enter your guess: ")
                        if(guess == computer_choice):
                            print(f"That's right its a {computer_choice}")
                            choice = 0
                        else:
                            print(f"sorry you are out of turns!\n")
                            print("You lose")
                            print(f"The correct answer is {computer_choice}")
                            choice = 0

    if(computer_choice == "Cat"):
        print("Clue 1 -> Small furry pet")
        guess = input("enter your guess: ")
        if(guess == computer_choice):
            print(f"That's right its a {computer_choice}")
            choice = 0
        else:
            print("Clue 2: Has whiskers.")
            guess = input("enter your guess: ")
            if(guess == computer_choice):
                print(f"That's right its a {computer_choice}")
                choice = 0
            else:
                print("Clue 3: Has soft paws")
                guess = input("enter your guess: ")
                if(guess == computer_choice):
                    print(f"That's right its a {computer_choice}")
                    choice = 0
                else:
                    print("Clue 4: Likes to chase mice")
                    guess = input("enter your guess: ")
                    if(guess == computer_choice):
                        print(f"That's right its a {computer_choice}")
                        choice = 0
                    else:
                        print("Clue 5: Says 'Meow!'")
                        guess = input("enter your guess: ")
                        if(guess == computer_choice):
                            print(f"That's right its a {computer_choice}")
                            choice = 0
                        else:
                            print(f"sorry you are out of turns!\n")
                            print("You lose")
                            print(f"The correct answer is {computer_choice}")
                            choice = 0


    if(computer_choice == "Dog"):
        print("Clue 1 -> Friendly pet.")
        guess = input("enter your guess: ")
        if(guess == computer_choice):
            print(f"That's right its a {computer_choice}")
            choice = 0
        else:
            print("Clue 2: Likes bones.")
            guess = input("enter your guess: ")
            if(guess == computer_choice):
                print(f"That's right its a {computer_choice}")
                choice = 0
            else:
                print("Clue 3: Has a wagging tail")
                guess = input("enter your guess: ")
                if(guess == computer_choice):
                    print(f"That's right its a {computer_choice}")
                    choice = 0
                else:
                    print("Clue 4: Guards the house")
                    guess = input("enter your guess: ")
                    if(guess == computer_choice):
                        print(f"That's right its a {computer_choice}")
                        choice = 0
                    else:
                        print("Clue 5: Says 'Woof!'")
                        guess = input("enter your guess: ")
                        if(guess == computer_choice):
                            print(f"That's right its a {computer_choice}")
                            choice = 0
                        else:
                            print(f"sorry you are out of turns!\n")
                            print("You lose")
                            print(f"The correct answer is {computer_choice}")
                            choice = 0

    if(computer_choice == "Eagle"):
        print("Clue 1 -> Big flying bird")
        guess = input("enter your guess: ")
        if(guess == computer_choice):
            print(f"That's right its a {computer_choice}")
            choice = 0
        else:
            print("Clue 2: Has very sharp eyes.")
            guess = input("enter your guess: ")
            if(guess == computer_choice):
                print(f"That's right its an {computer_choice}")
                choice = 0
            else:
                print("Clue 3: Has strong wings.")
                guess = input("enter your guess: ")
                if(guess == computer_choice):
                    print(f"That's right its an {computer_choice}")
                    choice = 0
                else:
                    print("Clue 4: Eats fish and small animals")
                    guess = input("enter your guess: ")
                    if(guess == computer_choice):
                        print(f"That's right its an {computer_choice}")
                        choice = 0
                    else:
                        print("Clue 5: Lives high in mountains or trees")
                        guess = input("enter your guess: ")
                        if(guess == computer_choice):
                            print(f"That's right its an {computer_choice}")
                            choice = 0
                        else:
                            print(f"sorry you are out of turns!\n")
                            print("You lose")
                            print(f"The correct answer is {computer_choice}")
                            choice = 0


    if(computer_choice == "Elephant"):
        print("Clue 1 -> Very big animal")
        guess = input("enter your guess: ")
        if(guess == computer_choice):
            print(f"That's right its an {computer_choice}")
            choice = 0
        else:
            print("Clue 2: Has a long trunk")
            guess = input("enter your guess: ")
            if(guess == computer_choice):
                print(f"That's right its an {computer_choice}")
                choice = 0
            else:
                print("Clue 3: Has big ears")
                guess = input("enter your guess: ")
                if(guess == computer_choice):
                    print(f"That's right its an {computer_choice}")
                    choice = 0
                else:
                    print("Clue 4: Has long white tusks")
                    guess = input("enter your guess: ")
                    if(guess == computer_choice):
                        print(f"That's right its an {computer_choice}")
                        choice = 0
                    else:
                        print("Clue 5: Eats plants and leaves")
                        guess = input("enter your guess: ")
                        if(guess == computer_choice):
                            print(f"That's right its an {computer_choice}")
                            choice = 0
                        else:
                            print(f"sorry you are out of turns!\n")
                            print("You lose")
                            print(f"The correct answer is {computer_choice}")
                            choice = 0

    if(computer_choice == "Fish"):
        print("Clue 1 -> Lives in water")
        guess = input("enter your guess: ")
        if(guess == computer_choice):
            print(f"That's right its a {computer_choice}")
            choice = 0
        else:
            print("Clue 2: Swims with fins.")
            guess = input("enter your guess: ")
            if(guess == computer_choice):
                print(f"That's right its a {computer_choice}")
                choice = 0
            else:
                print("Clue 3: Breathes through gills")
                guess = input("enter your guess: ")
                if(guess == computer_choice):
                    print(f"That's right its a {computer_choice}")
                    choice = 0
                else:
                    print("Clue 4: Has scales on its body")
                    guess = input("enter your guess: ")
                    if(guess == computer_choice):
                        print(f"That's right its a {computer_choice}")
                        choice = 0
                    else:
                        print("Clue 5: Lays eggs")
                        guess = input("enter your guess: ")
                        if(guess == computer_choice):
                            print(f"That's right its a {computer_choice}")
                            choice = 0
                        else:
                            print(f"sorry you are out of turns!\n")
                            print("You lose")
                            print(f"The correct answer is {computer_choice}")
                            choice = 0
                        
    if(computer_choice == "Shark"):
        print("Clue 1 -> Big fish with sharp teeth")
        guess = input("enter your guess: ")
        if(guess == computer_choice):
            print(f"That's right its a {computer_choice}")
            choice = 0
        else:
            print("Clue 2: Lives in the ocean")
            guess = input("enter your guess: ")
            if(guess == computer_choice):
                print(f"That's right its a {computer_choice}")
                choice = 0
            else:
                print("Clue 3: Swims very fast")
                guess = input("enter your guess: ")
                if(guess == computer_choice):
                    print(f"That's right its a {computer_choice}")
                    choice = 0
                else:
                    print("Clue 4: Has a big fin on its back")
                    guess = input("enter your guess: ")
                    if(guess == computer_choice):
                        print(f"That's right its a {computer_choice}")
                        choice = 0
                    else:
                        print("Clue 5: Has many sharp teeth")
                        guess = input("enter your guess: ")
                        if(guess == computer_choice):
                            print(f"That's right its a {computer_choice}")
                            choice = 0
                        else:
                            print(f"sorry you are out of turns!\n")
                            print("You lose")
                            print(f"The correct answer is {computer_choice}")
                            choice = 0


    if(computer_choice == "Dolphin"):
        print("Clue 1 -> Smart sea animal")
        guess = input("enter your guess: ")
        if(guess == computer_choice):
            print(f"That's right its a {computer_choice}")
            choice = 0
        else:
            print("Clue 2: Lives in the ocean")
            guess = input("enter your guess: ")
            if(guess == computer_choice):
                print(f"That's right its a {computer_choice}")
                choice = 0
            else:
                print("Clue 3: Looks like it is smiling")
                guess = input("enter your guess: ")
                if(guess == computer_choice):
                    print(f"That's right its a {computer_choice}")
                    choice = 0
                else:
                    print("Clue 4: Swims and jumps out of water")
                    guess = input("enter your guess: ")
                    if(guess == computer_choice):
                        print(f"That's right its a {computer_choice}")
                        choice = 0
                    else:
                        print("Clue 5: Makes clicking sounds")
                        guess = input("enter your guess: ")
                        if(guess == computer_choice):
                            print(f"That's right its a {computer_choice}")
                            choice = 0
                        else:
                            print(f"sorry you are out of turns!\n")
                            print("You lose")
                            print(f"The correct answer is {computer_choice}")
                            choice = 0


    if(computer_choice == "Monkey"):
        print("Clue 1 -> Has a long tail")
        guess = input("enter your guess: ")
        if(guess == computer_choice):
            print(f"That's right its a {computer_choice}")
            choice = 0
        else:
            print("Clue 2: Climbs trees")
            guess = input("enter your guess: ")
            if(guess == computer_choice):
                print(f"That's right its a {computer_choice}")
                choice = 0
            else:
                print("Clue 3: Likes bananas")
                guess = input("enter your guess: ")
                if(guess == computer_choice):
                    print(f"That's right its a {computer_choice}")
                    choice = 0
                else:
                    print("Clue 4: Uses hands to hold things")
                    guess = input("enter your guess: ")
                    if(guess == computer_choice):
                        print(f"That's right its a {computer_choice}")
                        choice = 0
                    else:
                        print("Clue 5: Very playful")
                        guess = input("enter your guess: ")
                        if(guess == computer_choice):
                            print(f"That's right its a {computer_choice}")
                            choice = 0
                        else:
                            print(f"sorry you are out of turns!\n")
                            print("You lose")
                            print(f"The correct answer is {computer_choice}")
                            choice = 0

