import random  # We need to make bot choose randomly, so we import random.


def get_bot_move():
    moves = ["rock", "paper", "scissors"]
    return random.choice(moves)

# Function to determine the winner


def determine_winner(user_move, bot_move):
    if user_move == bot_move:
        return "tie"
    elif (user_move == "rock" and bot_move == "scissors") or \
         (user_move == "scissors" and bot_move == "paper") or \
         (user_move == "paper" and bot_move == "rock"):
        return "user"
    else:
        return "bot"

# Function to allow player to choose how many rounds they want to play


def get_rounds():
    while True:
        try:
            rounds = int(input("Enter the number of rounds you want to play (only odd numbers): "))
            if rounds % 2 == 1:  # only odd numbers, so it's less likely to end in a tie
                return rounds
            else:
                print("Please enter an odd number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_user_move():
    while True:
        move = input("Enter your move (rock, paper, scissors): ").lower()
        if move in ["rock", "paper", "scissors"]:
            return move
        else:
            print("Invalid move. Please enter 'rock', 'paper', or 'scissors'.")


def play_game():
    rounds = get_rounds()
    user_score = 0
    bot_score = 0
    ties = 0

    for _ in range(rounds):
        user_move = get_user_move()
        bot_move = get_bot_move()
        print(f"Bot's move: {bot_move}")
        winner = determine_winner(user_move, bot_move)

        if winner == "user":
            user_score += 1
            print("You win this round!")
        elif winner == "bot":
            bot_score += 1
            print("Bot wins this round!")
        else:
            ties += 1
            print("This round is a tie!")

        print(f"Current Scores - You: {user_score}, Bot: {bot_score}, Ties: {ties}\n")

    if user_score > bot_score:
        print("Congratulations! You win the game!")
    elif bot_score > user_score:
        print("Bot wins the game! Better luck next time.")
    else:
        print("The game is a tie!")


if __name__ == "__main__":
    play_game()
