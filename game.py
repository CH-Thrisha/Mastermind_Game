import random

# Generate a random 4-digit number
num = random.randrange(1000, 10000)

print("Welcome to the 4-Digit Guessing Game!")
print("Type 'exit' or 'quit' at any time to end the game.")

# Get the initial guess from the player
guess = input("Guess the 4-digit number: ")

# Check if the player wants to exit
if guess.lower() in ['exit', 'quit']:
    print("Thank you for playing! Goodbye!")
else:
    n = int(guess)

    # Check if the player guessed correctly on the first try
    if n == num:
        print("Great! You guessed the number in just 1 try! You're a Mastermind!")
    else:
        # Counter for number of attempts
        ctr = 1

        # Loop until the correct number is guessed
        while n != num:
            # Initialize count of correct digits in correct positions
            count = 0
            n_str = str(n)
            num_str = str(num)

            # Compare digits and count matches
            for i in range(4):
                if n_str[i] == num_str[i]:
                    count += 1

            # Feedback based on correct digit count
            if count > 0:
                print(f"Not quite the number. But you did get {count} digit(s) correct!")
            else:
                print("None of the numbers in your input match.")

            # Prompt the player to guess again
            guess = input("Enter your next guess (or type 'exit' to quit): ")

            # Check if the player wants to exit
            if guess.lower() in ['exit', 'quit']:
                print("Thank you for playing! Goodbye!")
                break

            # Convert the guess to an integer
            n = int(guess)
            ctr += 1

        # When the correct number is guessed
        if n == num:
            print("You've become a Mastermind!")
            print(f"It took you only {ctr} tries.")




