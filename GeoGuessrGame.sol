// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GeoGuessrGame {
    address public owner;
    string public hint;
    bytes32 public locationHash;
    bool public gameEnded;
    
    mapping(address => uint256) public playerScores;
    mapping(address => bool) public hasGuessed;

    event GameStarted(string hint);
    event GameEnded(address winner, uint256 score);
    event GuessSubmitted(address player, uint256 distance);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    function startGame(string memory _hint, bytes32 _locationHash) public onlyOwner {
        require(!gameEnded, "Game already ended");
        hint = _hint;
        locationHash = _locationHash;
        gameEnded = false;
        emit GameStarted(_hint);
    }

    function submitGuess(uint256 latMicroDeg, uint256 lonMicroDeg) public {
        require(!hasGuessed[msg.sender], "Already guessed");
        require(!gameEnded, "Game already ended");

        // Here you'd calculate the distance between lat, lon and the correct location
        // For now we just simulate the score
        uint256 distance = calculateDistance(latMicroDeg, lonMicroDeg);
        
        playerScores[msg.sender] = distance;
        hasGuessed[msg.sender] = true;

        emit GuessSubmitted(msg.sender, distance);
    }

    function endGame(string memory correctLocation) public onlyOwner {
        require(!gameEnded, "Game already ended");

        // Compare the correct location hash to determine the winner
        address winner = getWinner();
        gameEnded = true;

        emit GameEnded(winner, playerScores[winner]);
    }

    function getWinner() private view returns (address) {
        address winner;
        uint256 bestScore = type(uint256).max;

        for (uint i = 0; i < players.length; i++) {
            if (playerScores[players[i]] < bestScore) {
                winner = players[i];
                bestScore = playerScores[players[i]];
            }
        }

        return winner;
    }

    function calculateDistance(uint256 latMicroDeg, uint256 lonMicroDeg) private pure returns (uint256) {
        // Implement Haversine formula here to calculate distance in meters
        // For now just returning a placeholder value
        return uint256(10000); // Placeholder distance
    }
}
