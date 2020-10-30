from common import w3, dai_address
import json
from pprint import pprint



# part 2 : load metamask account -> voir common.py


metaKey = '38dfc048f348c2f3ca2fa5e3558969f0a0b5dd3ed59106e8becd34594afcb617' #Add the new account key
metaAccount = w3.eth.account.from_key(metaKey)

print(metaAccount.address)

#part 2 : load Dai contract + afficher balance : 

with open("./contracts/abi/erc20_abi.json") as f:
    dai_abi = json.load(f)
dai_contract = w3.eth.contract(
    address= dai_address,
    abi= dai_abi
)
balance = dai_contract.functions.balanceOf(metaAccount.address).call()

print(w3.fromWei(balance, 'ether'))