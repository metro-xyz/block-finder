# pip3 install web3
# pip3 install python-dotenv

# main.py
import os
from dotenv import load_dotenv
from web3 import Web3

# https://web3py.readthedocs.io/en/latest/web3.eth.html#web3.eth.Eth.get_block

# Setup

load_dotenv()  # take environment variables from .env.

API_KEY = os.getenv('ALCHEMY_API_KEY')

alchemy_url = f"https://eth-mainnet.g.alchemy.com/v2/{API_KEY}"

w3 = Web3(Web3.HTTPProvider(alchemy_url))

# Print if web3 is successfully connected
print(w3.is_connected())

eth_mainnet_block_time = 12

# Get the latest block
latest_block = w3.eth.get_block('latest')
print(latest_block)

print(latest_block['number'])
print(latest_block['timestamp'])

# Get block by number
some_block = w3.eth.get_block(18000000)
print(some_block['number'])
print(some_block['timestamp'])
