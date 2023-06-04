from web3 import Web3
import os
from eth_account import Account

# Enable unaudited HD wallet features of the Account module
Account.enable_unaudited_hdwallet_features()

# Connect to the Ethereum node using Infura endpoint
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/'))

# Get the path to the file containing mnemonic phrases
filename = "mnemonic.txt"
filepath = os.path.join(os.getcwd(), filename)

# Read the mnemonic phrases from the file into a list
with open(filepath, 'r') as file:
    mnemonic_phrases = [line.strip() for line in file.readlines()]

# Loop through each mnemonic phrase and create an account object
results = []
for mnemonic_phrase in mnemonic_phrases:
    account = Account.from_mnemonic(mnemonic_phrase)

    # Get the private key in hexadecimal format from the account object
    private_key_hex = account.key.hex()

    # Get the Ethereum address from the account object
    address = w3.to_checksum_address(account.address)

    # Print the mnemonic phrase, private key, and Ethereum address
    result_string = f"{mnemonic_phrase}:{private_key_hex}:{address}"
    print(result_string)
    results.append(result_string)

# Write the results to a file
with open("result.txt", "w") as output_file:
    output_file.write("\n".join(results))
