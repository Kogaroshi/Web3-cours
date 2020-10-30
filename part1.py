from web3 import Web3, HTTPProvider
import json
from pprint import pprint

# part 1 : test web3

w3 = Web3(HTTPProvider("http://37.187.153.186:8554",request_kwargs={'timeout':60}))
print(w3.isConnected())

# part 1 : block number 

print(w3.eth.blockNumber)

# part 1 : création wallet 

#account = w3.eth.account.create('BTRE1B45T1B4TG6ZBTZ641BTRZ6TBERZ6Z')
#print(account.address)
#print(account.key)
#pprint(w3.eth.account.encrypt(account.key, 'password'))

#part 1 : check wallet balance

with open('./account/encrypted_key.json') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, 'password')
localAccount = w3.eth.account.from_key(private_key)

balance = w3.eth.getBalance(localAccount.address)

print(balance)

#Comme c'est difficile de lire les wei, on peut convertir ça : 
balance = w3.fromWei(w3.eth.getBalance(localAccount.address), 'ether')

print(balance)

# part 1 : send funds 

"""metaAddress = '' #To add

signed_tx = w3.eth.account.signTransaction({
    'to': metaAddress,
    'from': localAccount.address,
    'value': w3.toWei(1, 'ether'), 
    'nonce': w3.eth.getTransactionCount(localAccount.address),
    'gasPrice': w3.eth.gasPrice,
    'gas': 100000
},localAccount.key)

result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(result.hex())
txReceipt = w3.eth.waitForTransactionReceipt(result)
pprint(txReceipt)

balance = w3.fromWei(w3.eth.getBalance(localAccount.address), 'ether')
print(balance)"""