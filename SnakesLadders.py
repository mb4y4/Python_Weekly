import random

def roll_dice():
    return random.randint(1, 6)

def snakes_and_ladders(position):
    snakes_and_ladders_dict = {
        16: 6,
        47: 26,
        49: 11,
        56: 53,
        62: 19,
        64: 60,
        87: 24,
        93: 73,
        95: 75,
        98: 78
    }

    if position in snakes_and_ladders_dict:
        new_position = snakes_and_ladders_dict[position]
        if new_position > position:
            print(f"Wow! You found a ladder! Climb from {position} to {new_position}.")
        else:
            print(f"Oh no! You landed on a snake! Slide from {position} to {new_position}.")
        return new_position
    else:
        return position

def display_board(player_position):
    print("\n" + "-" * 30)
    for i in range(9, 0, -1):
        row = "|"
        for j in range(10 * (i - 1) + 1, 10 * i + 1):
            if j == player_position:
                row += " P |"
            else:
                row += f" {j} |"
        print(row + "\n" + "-" * 30)

def main():
    player_position = 1

    print("Welcome to Snakes and Ladders!")

    while player_position < 100:
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print(f"You rolled a {dice_roll}.")

        player_position += dice_roll
        player_position = snakes_and_ladders(player_position)

        if player_position > 100:
            player_position = 200 - player_position  # Bounce back if overshooting 100

        display_board(player_position)

    print("Congratulations! You reached 100. You win!")

if __name__ == "__main__":
    main()
