from web3 import Web3

# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# GeoGuessr contract address and ABI
contract_address = '0xYourContractAddressHere'
contract_abi = '[...]'  # ABI of the GeoGuessr contract

# Initialize contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# User's Ethereum address and private key
my_address = '0xYourAddressHere'
private_key = 'YourPrivateKeyHere'

# Function to end game and reward winner
def end_game(correct_location: str):
    # Build the transaction
    transaction = contract.functions.endGame(correct_location).buildTransaction({
        'chainId': 1,
        'gas': 2000000,
        'gasPrice': w3.toWei('20', 'gwei'),
        'nonce': w3.eth.getTransactionCount(my_address),
    })

    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

    # Send the transaction
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f"Game ended, transaction hash: {txn_hash.hex()}")

# Example: ending the game with the correct location
end_game('0xCorrectLocationHashHere')
