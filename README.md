# Coin Flipper Game

## Overview

Welcome to the Coin Flipper Game! This is an interactive game developed using the Python library pygame. In this game, you will have the opportunity to flip a virtual coin and guess whether it's biased towards heads or not. Your goal is to accumulate the highest score possible by making the correct guesses and managing your health effectively.

## Getting Started

To play the game, follow these steps:

1. **Install Python and pygame**:

   - Make sure you have Python 3.x installed on your computer.
   - Install the pygame library by running the following command:

     ```bash
     pip install pygame
     ```

2. **Clone the Repository**:

   - Clone or download this GitHub repository to your local machine.

3. **Run the Game**:

   - Navigate to the directory where you've cloned or downloaded the game.
   - Run the game by executing the `coin_flip_game.py` script:

     ```bash
     python coin_flip_game.py
     ```

## Game Rules

Here's how to play the Coin Flipper Game:

- You start the game with 100 health and a score of 0.

- You have two options for flipping the coin:
  - **Flip Once**: This option allows you to flip the coin once, which consumes 1 health point.
  - **Flip Five Times**: This option allows you to flip the coin five times in a row, consuming 5 health points.

- After each flip, you need to guess whether the coin is biased towards heads or not by clicking the "Biased" or "Unbiased" buttons.
  - If you guess correctly, your score increases by 1 point, and you lose 10 health points.
  - If you guess incorrectly, you lose 10 health points.

- The game continues until your health reaches 0.

- Your goal is to achieve the highest score by making consecutive correct guesses and managing your health wisely.

## Customization

You can customize the game by modifying the following variables in the `coin_flip_game.py` script:

- `initial_health`: Set the initial health of the player.
- `coin_bias_probability`: Adjust the probability of a biased coin coming up (default is 0.5, which means a 50% chance of a biased coin).

## Winning and Restarting

- There is no specific "winning" condition in this game; the goal is to achieve the highest score possible.

- If you run out of health, you can restart the game by clicking the "Restart" button.

## Have Fun!

Enjoy playing the Coin Flipper Game! Test your intuition and aim for a high score. If you have any questions or feedback, feel free to reach out. Good luck!
