from common import w3, dai_address, postit_address, metaAccount
import json
from pprint import pprint


# part 3 : load postit contract + afficher message

with open("./contracts/abi/post-it-abi.json") as f:
    postit_abi = json.load(f)

postIt = w3.eth.contract(
    address = postit_address,
    abi = postit_abi
)

print(postIt.functions.getMessage().call())


# part 3 : deployer contract

"""
with open("./contracts/abi/post-it-abi.json") as f:
    postit_abi = json.load(f)
with open("./contracts/bytecode/post-it-bytecode.json") as f:
    postit_bytecode = json.load(f)['object']

PostIt = w3.eth.contract(abi=postit_abi, bytecode=postit_bytecode)
tx_dict = PostIt.constructor('1st message').buildTransaction({
    'from' : metaAccount.address,
    'nonce' : w3.eth.getTransactionCount(metaAccount.address)
})

tx = w3.eth.account.signTransaction(tx_dict, metaAccount.key)
result = w3.eth.sendRawTransaction(tx.rawTransaction)
print(result.hex())
txReceipt = w3.eth.waitForTransactionReceipt(result)
pprint(txReceipt)
print(txReceipt['contractAddress'])
"""

# part 3 : changer message dans contract
"""
tx_dict = postIt.functions.setMessage("new message").buildTransaction({
    'from': metaAccount.address,
    'nonce': w3.eth.getTransactionCount(metaAccount.address)
})
tx = w3.eth.account.sign_transaction(tx_dict, metaAccount.key)
result = w3.eth.sendRawTransaction(tx.rawTransaction)
receipt = w3.eth.waitForTransactionReceipt(result)
pprint(receipt)
print(postIt.functions.getMessage().call())
"""

# part 3 : Event dans une transaction

tx_hash = "0xa92f71f18ff2c4c5ea2225bf4a5dc3617442be078df22661092a841a712116b8" #To change suring class

receipt = w3.eth.getTransactionReceipt(tx_hash)

tx_logs = receipt['logs']

print(tx_logs)

event = postIt.events.NewMessage().processReceipt(receipt)[0]

pprint(event['args'])
pprint(event['args']['_message'])