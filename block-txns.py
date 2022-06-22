import time
from web3 import Web3

web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

print(web3.isConnected())

def print_all(web3):
    block = web3.eth.getBlock('latest').__dict__
    print(block['number'])
    print(len(block['transactions']))

while True:
    time.sleep(1)
    print_all(web3)

