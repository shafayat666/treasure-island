# Treasure Island 🏝️

Welcome to **Treasure Island**! This is a simple text-based adventure game where your mission is to find the hidden treasure. Make your choices carefully, as every decision can lead you closer to the treasure or to game over!

## Table of Contents

- [How to Play](#how-to-play)
- [Game Features](#game-features)
- [Installation](#installation)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)

## How to Play

1. When the game starts, you will be greeted with a prompt asking you to make a choice.
2. Read the scenario and type in your answer when prompted.
3. Make sure to type your answers correctly (e.g., "left", "right", "wait", "swim", "red", "yellow", "blue", "yes", "no").
4. Your decisions will lead you through different paths — some will help you find the treasure, while others will end your journey.
5. You can play the game multiple times and try different paths to discover all possible outcomes.

## Game Features

- **Interactive Storytelling**: Engage in an exciting text-based adventure where every decision counts.
- **Multiple Paths**: Explore different scenarios and endings based on your choices.
- **Replayable**: Play again and again to uncover new paths and outcomes.

## Installation

1. Make sure you have Python installed on your machine. If not, [download and install Python](https://www.python.org/downloads/).
2. Clone this repository or download the `treasure_island.py` file.

    ```bash
    git clone https://github.com/shafayat666/treasure-island.git
    ```
3. Navigate to the project directory.
    ```bash
    python main.py
    ```
## Code Explanation

The code is structured using functions to handle different scenarios in the game. Here is a brief explanation of the approach and logic:

1. **Introduction and Initial Setup**: 
   - The game starts by printing a welcome message with the title "Treasure Island".
   - The `choose_action` function is called to ask the user to make the first choice.

2. **Scenario-Based Functions**:
   - The game flow is handled using separate functions for each scenario:
     - `choose_action()`: The initial function that asks whether the player wants to go "left" or "right".
     - `lake_scenario()`: Triggered when the player chooses "left". It presents the next decision (whether to "wait" or "swim").
     - `house_scenario()`: If the player waits for a boat, they reach the house and must choose a door color ("red", "yellow", or "blue").

3. **Handling Unexpected Input**:
   - If the user enters an invalid response, they are prompted to enter a valid choice, and the respective function is called again to re-ask the question.
   - Recursion is used to repeat the question if the input is incorrect. This approach ensures that the game progresses only when valid input is provided.

4. **Game Loop**:
   - The game runs in a loop using `while game_is_on`. The `continue_game` function prompts the user to play again after finishing each game.
   - Depending on the player's choice, the game either starts over or ends with a thank you message.

This modular approach using functions helps to keep the code clean, organized, and easy to understand. Each scenario is isolated in its own function, making it simple to extend or modify the game in the future.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are always welcome!


