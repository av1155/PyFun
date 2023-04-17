import random
# Imports random so random numbers can be generated in the program.


# This function displays the general project information including my name, email, the course, my major, and a general introduction to the final project. It is called in the main function.
def display_project_information():
    print("\nAndrea A. Venti Fuentes")
    print("This project includes a lottery number generator, a Pig Latin translator, and a rock-paper-scissors game. The program prompts the user to choose between these functions and displays the generated output or prompts for user input accordingly.")

    # Lists a valid response and prompts the user to input it through another function. If the user inputs anything other than "now", the program will tell the user that their input is invalid and to choose a valid option.
    valid_response_1 = ["now"]
    user_choice = prompt_user(
        "\nType 'now' when you are ready to return to the main menu...\n> ", valid_response_1)

    if user_choice == "now":
        main()


# This function, which is called in the main function, is a lottery number generator which generates 6 random numbers and displays them at the end. The first five numbers are generated and appended in a list until they are all unique. After the five numbers are appended and sorted in ascending order, the loop stops, the function then appends a last sixth number to the end. The first five random numbers are between 1 and 69, and the last random number is between 1 and 26.
def lottery_number_generator():
    print("\nWelcome to the lottery number generator!\n")

    # Empty list created.
    lottery_numbers_list = []
    # Loop for generating the first five unique numbers.
    while len(lottery_numbers_list) < 5:
        new_number = random.randint(1, 69)
        # If statement that checks if the newly generated numbers already exists in the list, if it does, it generates a new one until they are all unique. At the end, they are all appended to the list.
        if new_number not in lottery_numbers_list:
            lottery_numbers_list.append(new_number)

    # The five numbers are sorted in ascending order.
    lottery_numbers_list.sort()
    # A new last "power ball" number is generated and appended at the end of the list that at this point contains only five random unique numbers.
    powerball_number = random.randint(1, 26)
    lottery_numbers_list.append(powerball_number)

    # Two `print()` stamenets are used for displaying the lottery numbers collectively. The * before the variable is used so that the numbers are displayed without the brackets from the list, and the numbers are displayed with spaces in between.
    print("The lottery numbers are...")
    print(*lottery_numbers_list)

    # or

    # for number in lottery_numbers_list:
    #     print(f"{number} ", end="")

    # The user is asked if they want to generate a new lottery number or not. If they do, the function is called again, if they don't, the main function is called.
    valid_responses_2 = ["yes", "y", "no", "n"]
    user_choice = prompt_user(
        "\nDo you want to generate a new lottery number? (y/n)\n> ", valid_responses_2)

    if user_choice == "yes" or user_choice == "y":
        lottery_number_generator()
    elif user_choice == "no" or user_choice == "n":
        main()


# Function used to translated a sentence to Pig Latin which is called in the main function.. The first letter of each word is moved to the end of the word and a, "ay" is added to the end of each word.
def pig_latin():
    print("\nWelcome to the Pig Latin translator!")

    while True:

        # Prompt that asks the user for a sentence to be translated.
        sentence = input(
            "\nWrite a sentence to translate it to Pig Latin!\n> ").lower()

        # Splits all the words that the user wrote into a list. Spaces are removed and only the words are kept, separated, into their own "value".
        sentence_list = sentence.split()

        # Another empty list is created that will be used to store the translated sentence later.
        translated_sentence = []

        # For loop that goes through each word in the "sentence_list" that contains all the words and moves the first letter of each word to the end, and adds "ay" to the end of them.
        for word in sentence_list:
            word = word[1:] + word[0] + "ay"
            translated_sentence.append(word)

        # The updated variable below and the print statement are used to output the final result of the function and it join all the words from the "translated_sentence" list with a space in between and update the variable. This way the words do not like this: ogdayogday, but they look like this: ogday ogday.
        translated_sentence = " ".join(translated_sentence)
        print(f"\n{translated_sentence}\n")

        # The user is asked if they want to translate a new sentence or not. If they do, the function is called again, if they don't, the main function is called.
        valid_responses_3 = ["yes", "y", "no", "n"]
        user_choice = prompt_user(
            "Do you want to translate a new sentence? (y/n)\n> ", valid_responses_3)

        if user_choice == "yes" or user_choice == "y":
            pig_latin()
        elif user_choice == "no" or user_choice == "n":
            main()


# Function for the rock, paper, scissors game which is called in the main function.
def rock_paper_scissors_game():
    print("\nWelcome to the Rock, Paper, Scissors game!")

    # While True loop used to restart the game if the person wants to replay at the end of the game.
    while True:

        # While True loop that asks the user how many turns they want to play for, it also checks if the user inputs anything else but a number, which would return an error; if there is an error, the program will ask the user again to input a valid number.
        while True:
            try:
                number_of_turns = int(
                    input("\nHow many turns do you want to play? "))
                break
            except ValueError:
                print("\nPlease enter a valid number.")

        # The game has a score system, and because of the user decides how many turns they want to play for, the turn count records the turns that have passed and stops the game when that number is reached. This also resets the score and the turn count if the user wants to replay the game.
        user_wins = 0
        computer_wins = 0
        turn_count = 0

        # While True loop for the main game. The loop ends when the turn count equals to the number of turns the user chose.
        while True:

            # The computer guess is assigned to a random number between 1 and 3, which is turned to a string in the process so it can be used later to print the guess of the computer. This is why an options dictionary is created too, so that the users input, which is a number, and the computer guess, another number, are both assigned to rock, paper, or scissors. The users number was always a string, that is why only the computer number is turned to a string.
            computer_guess = str(random.randint(1, 3))
            options = {"1": "rock", "2": "paper", "3": "scissors"}

            #  Records the user input as a number, and gets assigned to rock, paper, or scissors later when printed through the dictionary. If the user input is anything except 1, 2, or 3, it will ask the user to try again with the continue statement.
            user_input = input(
                "\nChoose: \n- (1) Rock\n- (2) Paper\n- (3) Scissors\n> ").lower()
            if user_input not in options:
                print("\nInvalid input. Try again :)")
                continue

            # Adds one turn to the counter every time the user plays. Because it is placed after "continue" it will not count invalid inputs in the turn counter.
            turn_count += 1

            # Displays the choice of the user and the choice of the computer (becomes rock, paper, or scissors through the dictionary instead of displaying a number).
            print(
                f"\nYou picked {options[user_input]}! Computer picked {options[(computer_guess)]}!")

            # If statement that determines when the user wins. Adds a point to the overall game for the user.
            if (user_input == "1" and computer_guess == "3") or (user_input == "2" and computer_guess == "1") or (user_input == "3" and computer_guess == "2"):
                user_wins += 1
                print(f"You won!")

            # If statement that determines when the computer wins. Adds a point to the overall game for the computer.
            if (computer_guess == "1" and user_input == "3") or (computer_guess == "2" and user_input == "1") or (computer_guess == "3" and user_input == "2"):
                computer_wins += 1
                print(f"You lost!")

            # If statement that determines when there is a tie, and a turn is subtracted from the turn counter. Does not count towards the amount of turns selected at the start of the game.
            if user_input == computer_guess:
                turn_count -= 1
                print("You tied! Try again :)")
                continue

            # End the game when the number of turns specified by the user is reached!
            if turn_count == number_of_turns:
                break

        # Calculate the winner based on the number of points earned by the user and the computer. If both have the same number of points, the game ends as a tie (rematch is offered later though!). Otherwise, the player with the higher number of points wins. The results are printed out at the end of the game.
        if user_wins == computer_wins:
            print(
                f"\nTie! You got {user_wins} point/s, and the computer got {computer_wins} point/s.\n")
        else:
            if user_wins > computer_wins:
                print(
                    f"\nYou won with {user_wins} point/s! The computer got {computer_wins} point/s.\n")
            else:
                print(
                    f"\nYou lost! The computer got {computer_wins} point/s! You got {user_wins} point/s :(\n")

        # Asks the user if they want to play again. If they do, the game restarts. If they don't, the game ends and the user is sent back to the main menu.
        valid_responses_4 = ["yes", "y", "no", "n"]
        user_choice = prompt_user(
            "Do you want to play again? (y/n)\n> ", valid_responses_4)

        if user_choice == "yes" or user_choice == "y":
            rock_paper_scissors_game()
        elif user_choice == "no" or user_choice == "n":
            print("Goodbye!")
            main()


# Function that grabs the arguments when called and validates the input. If the input is valid (corresponding to the availale options that are in independent lists for each function) then this function returns the input. If it is invalid, it returns an error message and asks the user to try again.
def prompt_user(prompt_message, valid_responses):
    while True:
        user_input = input(prompt_message).lower()
        if user_input in valid_responses:
            return user_input
        else:
            print("\nInvalid input. Choose a valid option.")
            continue


# Main function where the main menu is stored. The main menu asks the user what program mode they would like to use. For ease of use, the  modes are paired with a number, so that the user does not have to type a lot. The modes are also displayed in a vertical list so that it is easier to read and a `\n> ` is used at the end so that the user can type the choice in a visually appealing prompt.
def main():
    print("\nWelcome to my final project!")

    while True:
        program_mode_choice = input(
            f"\nChoose an option from the main menu:\n- (1) Display Project Information \n- (2) Lottery Number Generator \n- (3) Pig Latin \n- (4) Rock Paper Scissors Game \n- (5) Exit Program \n> ")

        # The program modes are all separated into different if statements so that they all direct the user to the desired "function". An "Exit Program" mode is also created so that the user can exit when they are done using the program.
        if program_mode_choice == "1":
            display_project_information()

        elif program_mode_choice == "2":
            lottery_number_generator()

        elif program_mode_choice == "3":
            pig_latin()

        elif program_mode_choice == "4":
            rock_paper_scissors_game()

        elif program_mode_choice == "5":
            quit()

        # Input validation that checks if anything inside except the valid_options list is inputted. If it is, then the user is redirected to the main menu to choose a valid option.
        valid_options = ["1", "2", "3", "4", "5"]
        if program_mode_choice != valid_options:
            print("\nInvalid input. Choose a selection from the main menu.")
            continue


# The __name__ variable holds the name of the document with the value __main__. This checks if the file is being run directly by python or if it is being imported.
if (__name__ == "__main__"):
    main()
