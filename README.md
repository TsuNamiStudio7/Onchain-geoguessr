# Onchain GeoGuessr

This is an onchain version of the popular game *GeoGuessr*. Players try to guess a hidden location based on a hint, and the game rewards the closest guess.

## Smart Contract

The smart contract manages the game logic, including:

- Starting the game with a hint and location hash
- Allowing players to submit their guesses (in the form of latitude and longitude)
- Ending the game and rewarding the winner

## Python Scripts

### `submit_guess.py`
Allows players to submit their guesses (latitude and longitude) to the smart contract.

### `end_game.py`
The owner can end the game, reveal the correct location, and reward the winner.

### `utils.py`
Contains utility functions, such as the Haversine formula for calculating distances between two points on Earth.

### `tests.py`
Contains unit tests for core logic like distance calculation.

## Requirements

- Python 3.x
- Web3.py
- Solidity Compiler (for deploying contracts)

## Instructions

1. Deploy the `GeoGuessrGame.sol` smart contract.
2. Use `submit_guess.py` to submit your guess to the contract.
3. Use `end_game.py` to reveal the correct location and reward the winner.
