# Stone Paper Scissor Game

# import random module to genrate computer value randomly
import random as rd

x = 0
y = 0
z = 0
i = 1
print("= = = = = = = = = = Stone Paper Scissor = = = = = = = = = =")

while True:
    # Looping 5 times
    # This loop for playing 5 matches
    while i <= 5:

        print("Please choose any one")
        print("1.Stone")
        print("2.Paper")
        print("3.scissor")

        # Take the input from user
        a = int(input())
        # Initialize value of user choice a variable
        # And print user choice
        if a == 1:
            print("Your choice is = Stone")
        elif a == 2:
            print("Your choice is = Paper")
        elif a == 3:
            print("Your choice is = Scissor")

        #
        if a <= 3:
            # Computer chooses randomly any number
            # among 1,2,3 using radint method of random module.
            b = rd.randint(1, 3)
            # print computer choice
            if b == 1:
                print("Computer choice is = Stone")
            if b == 2:
                print("Computer choice is = Paper")
            if b == 3:
                print("Computer choice is = Scissor")

            # Condition for winning
            if a != b:
                # for user winning
                if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
                    print("--------You Win--------")
                    x = x + 1
                # for computer winning
                elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
                    print("--------Computer Win--------")
                    y = y + 1
            else:
                print("--------Match tie---------")
                z = z + 1
        else:
            print("invalid choice")
        print("")
        i = i + 1
    # Result for winning
    print("You win", x, " matches")
    print("Computer win ", y, " matches")
    print("Match tie ", z, " times")
    print("")
    # final result for winning
    if x > y:
        print("=====You win the series=====")
    elif x < y:
        print("=====Computer win the series=====")
    else:
        print("=====Series tie=====")

    print()
    print("Do you want to play again?(y/n)")
    ans = input()
    # if user input n then condition is true and user coming out the loop.
    if ans == "n" or ans == 'N':
        break
