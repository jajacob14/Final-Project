import random
import time
import sys

# Function to simulate rolling dice
def roll_dice():
    """
    Rolls three dice and returns the result as a list.
    """
    dice = [random.randint(1, 6) for _ in range(3)]
    print(f"Dice rolled: {dice}")
    return dice

# Function to check if all dice are the same (tuple out)
def is_tuple_out(dice):
    """
    Checks if all dice have the same value, indicating a "TUPLE OUT".
    """
    return dice[0] == dice[1] == dice[2]

# Function to calculate score
def calculate_score(dice):
    """
    Calculates the score based on the dice values.
    Returns 0 if all dice are the same (TUPLE OUT); otherwise, returns the sum of the dice.
    """
    return 0 if is_tuple_out(dice) else sum(dice)

# Function to measure processing time
def measure_processing_time():
    """
    Simulates a computation and measures processing time.
    """
    start_time = time.process_time()
    dice = roll_dice()
    score = calculate_score(dice)
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    print(f"Processing time: {elapsed_time:.5f} seconds")
    return elapsed_time

# Function to add time stamps
def add_time_stamp():
    """
    Generates a timestamp for when the dice are rolled.
    """
    current_time = time.localtime()
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    print(f"Dice rolled at: {time_stamp}")
    return time_stamp

# Main game loop
def main():
    """
    Runs the main dice game, integrating timing analysis and timestamping.
    Checks if the seaborn module is available before starting.
    """
    # Check if seaborn is installed
    try:
        __import__('seaborn')
        print("Seaborn is installed and ready to use.")
    except ImportError:
        print("Seaborn is not installed. Run 'pip install seaborn' to install it.")
        sys.exit(1)
    
    print("Welcome to the Time Trial Dice Game!")
    player_score = 0
    target_score = 50

    while player_score < target_score:
        print("\nRolling the dice...")
        time_stamp = add_time_stamp()
        elapsed_time = measure_processing_time()
        dice = roll_dice()
        score = calculate_score(dice)
        player_score += score
        print(f"Player score: {player_score} (Score from this round: {score})")
        print(f"Roll timestamp: {time_stamp}, Time taken for this round: {elapsed_time:.5f} seconds")

        if is_tuple_out(dice):
            print("TUPLE OUT! Turn ends with a score of 0 for this round.")
            break

    print(f"\nGame over! Final score: {player_score}")

# Entry point for the program
if __name__ == "__main__":
    main()
