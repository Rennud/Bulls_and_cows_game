import random as r
import datetime

'''BULLS AND COWS GAME RULES:
The player guesses a four-digit number.
If the number and index hit correctly, the program will return the number of Bull / Bulls 
If player hits the correct number but does not hit the index, the program return the number of Cow / Cows
The game ends when the player correctly guesses all numbers, including the correct indexes
In other words, the program will return 4 Bulls'''

SEPARATOR = 40 * "-"

print('Hi there!')
print(SEPARATOR)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(SEPARATOR)

# Generating a unique number without duplicate numbers
while True:
    secret_num = r.sample(range(1, 9), 4)
    if len(set(secret_num)) != len(secret_num):
        continue
    else:
        break


def play_game(num_for_guess):
    # Function that solves the entire game. Requires a variable that is a guessed number.
    attempts = 0
    # A loop that ends only when a player guesses a number
    while True:
        try:
            bulls = 0
            cows = 0
            save_guess = []
            attempts += 1
    # If the player does not meet the conditions for correct entry, he is warned and asked to re-enter
            while True:
                player_guess = input('ENTER FOUR NUMBERS: ')
                if len(player_guess) > 4 or len(player_guess) < 4 or player_guess[0] == '0' or len(
                        set(player_guess)) != len(player_guess):
                    print(
                        'Wrong input. Your guess must contains precisely 4 numbers, must not start with 0 and every '
                        'number must be unique.')
                    print(SEPARATOR)
                else:
                    break
    # A loop that stores individual numbers from the input in a list and changes the data type to int
            for i in range(4):
                save_guess.append(int(player_guess[i]))
    # A loop that checks whether a player has hit the index or a number or both
    # If so, one for each occurrence is added to the bulls or cows variable according to the rules of the game
            for i, num in enumerate(save_guess):
                if save_guess[i] == num_for_guess[i]:
                    bulls += 1
                if num in num_for_guess and not save_guess[i] == num_for_guess[i]:
                    cows += 1
            if bulls == 1 or bulls == 0:
                bull_str = 'bull'
            else:
                bull_str = 'bulls'
            if cows == 1 or cows == 0:
                cows_str = 'cow'
            else:
                cows_str = 'cows'
            print(f'{bulls} {bull_str}, {cows} {cows_str}')
            print(SEPARATOR)
    # If the bulls variable equals four, it means that the player guessed the secret number The program inserts the
    # current date and time into the Statistics.txt file with the number of attempts for each game played
            if bulls == 4:
                print(f"Correct, you've guessed the right number in {attempts} guesses!")
                if attempts < 3:
                    print('Amazing result! :)')
                elif 3 < attempts < 8:
                    print('Average result.')
                else:
                    print('That is not good result. :(')
                date = datetime.datetime.now()
                date_edit = date.strftime('%d/%m/%Y %X')
                with open('Statistics.txt', 'a') as sta:
                    sta.write(f'{date_edit} - Number o attempts: {attempts}\n')
            while bulls == 4:
                next_game = input("Do you want to play again? Type 'y' for yes or 'n' for no: ")
                if next_game == 'n':
                    print('Hope you enjoy the game.')
                    print('Quitting the game.')
                    exit()
                elif next_game == 'y':
                    break
                else:
                    print('Wrong input')
        except ValueError:
            print('Wrong input. You must type only numbers.')


play_game(secret_num)
