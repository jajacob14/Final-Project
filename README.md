Final Project 126
Dice Game

A simple dice game for one or multiple players. The game involves rolling dice, making strategic decisions on re-rolls, and competing to achieve the highest score.

Features

Supports multiple players: Play with friends or against yourself.

Automatic dice rolling and scoring: Rolls are generated programmatically for fairness.

Special conditions:

TUPLE OUT: If all three dice show the same value, the player scores 0 for the turn.

Fixed Dice: If at least two dice have the same value, the player cannot re-roll those dice.

Strategic re-rolls: Players can decide which dice to re-roll for better scores.

Configurable target score: Adjust the goal for winning based on preferences.

How to Play

Setup:

Enter the number of players when prompted.

Decide the target score for winning (default is 50).

Player Turn:

Roll three dice automatically.

Decide whether to re-roll any of the dice or keep the current roll.

Repeat until one of the following occurs:

The player decides not to re-roll.

A "TUPLE OUT" or "Fixed Dice" condition occurs.

The turn ends, and the score is added to the player's total.

Winning:

The first player to reach or exceed the target score wins the game.

Rules

TUPLE OUT:

If all dice have the same value, the player's score for that turn is 0.

Fixed Dice:

If at least two dice have the same value, those dice are considered "fixed," and the player cannot re-roll them.

Scoring:

If neither condition occurs, the player's score is the sum of the dice values.

How to Run

Clone the repository or download the game script.

Run the script using Python:

python dice_game.py

Timing Analysis

The game includes timing features to measure CPU time for performance analysis. At the end of each game, the total CPU time used during gameplay is displayed.

Dependencies

Python 3.x

Seaborn (optional, for visualizations)

Installing Dependencies

If Seaborn is required for advanced visualizations:

pip install seaborn

Example Output

Player 1's turn:
Dice rolled: 2, 5, 3
Re-roll dice 2 (current value: 5)? (y/n) y
Dice after re-roll: 2, 6, 3
Player 1's score: 11

Player 2's turn:
Dice rolled: 4, 4, 4
TUPLE OUT! You score 0 points.

Player 1 wins with a total score of 50!
Total CPU time taken: 12.45 seconds

License

This game is distributed under the MIT License.

