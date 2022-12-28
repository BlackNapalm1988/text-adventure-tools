# Import the Interpreter from the tools module
from tools import Interpreter

# Setup you scripts as TXT documents using the RPGML scripting language
scripts = {
    "Intro"         :  "storyline/intro.txt",
    "Chapter One"   :  "storyline/chapter_one.txt",
    "Chapter Two"   :  "storyline/chapter_two.txt",
    "Closing"       :  "storyline/closing.txt",
}

# Create your storyline and pass in your scripts dictionary of file paths
storyline = Interpreter(scripts)

# Run the start method to build the branches, options from your script file
storyline.start()


# Set a couple variables to create a basic game
player_alive = True
player_won = False

# Check if the player is alive and begins the game
if player_alive:

    # This is your game loop, check the branches list for all options and run your
    for branch in storyline.branches:

        for options in branch:

            while "FIRST BRANCH" in options:

                # Take Player input and store as a response variable
                response = storyline.prompt()

                if response in options == "LOOK AROUND":
                    print("You look around")

                if response in options == "GO BACK TO SLEEP":
                    print("You go back to sleep")

                if response in options == "SCREAM FOR HELP":
                    print("You scream for help!")

            else:
                print("I didn't understand your response, try again!")

        # if "SECOND BRANCH" in branch:
        #     print("2 Your Options Are: ", branch[1], branch[2])

        # if "THIRD BRANCH" in branch:
        #     print("3 Your Options Are: ", branch[1], branch[2], branch[3])

        # if "FOURTH BRANCH" in branch:
        #     print("4 Your Options Are: ", branch[1], branch[2], branch[3])

        # if "FIFTH BRANCH" in branch:
        #     print("5 Your Options Are: ", branch[1], branch[2], branch[3])

    else:
        player_alive = False