import random


def generate_number(length):
    """Generate a random multi-digit number of the specified length."""
    return ''.join(random.choices('0123456789', k=length))


def get_feedback(guess, secret):
    """Provide feedback on the guess compared to the secret number."""
    correct_digits = sum(1 for g, s in zip(guess, secret) if g == s)
    return correct_digits


def mastermind_game():
    print("Welcome to the Mastermind Game!")

    # Player 1 sets the number
    length = int(input("Player 1, enter the length of the number you want to set: "))
    secret_number = generate_number(length)
    print("Player 1 has set the number. Player 2, start guessing!")

    # Player 2 guesses the number
    attempts = 0
    while True:
        guess = input("Player 2, enter your guess: ")
        attempts += 1

        if guess == secret_number:
            print(
                f"Congratulations Player 2! You've guessed the number {secret_number} correctly in {attempts} attempts.")
            break
        else:
            correct_count = get_feedback(guess, secret_number)
            print(f"You got {correct_count} digits correct. Keep trying!")

    # Switch roles
    print("Now it's Player 2's turn to set the number. Player 1, start guessing!")
    secret_number = input("Player 2, enter the number you want Player 1 to guess: ")

    attempts_player_1 = 0
    while True:
        guess = input("Player 1, enter your guess: ")
        attempts_player_1 += 1

        if guess == secret_number:
            print(
                f"Congratulations Player 1! You've guessed the number {secret_number} correctly in {attempts_player_1} attempts.")
            break
        else:
            correct_count = get_feedback(guess, secret_number)
            print(f"You got {correct_count} digits correct. Keep trying!")

    # Determine the winner
    if attempts_player_1 < attempts:
        print("Player 1 wins and is crowned Mastermind!")
    else:
        print("Player 2 wins!")


# Start the game
mastermind_game()
