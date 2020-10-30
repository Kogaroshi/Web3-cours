from common import w3, dai_address, metaAccount, uniswap_router2_address
import json
import time
from pprint import pprint

with open("./contracts/abi/uniswap_router2_abi.json") as f:
    uni_abi = json.load(f)

uniRouter = w3.eth.contract(
    address = uniswap_router2_address,
    abi = uni_abi
)

amount = 0.2

#Parce que le smart contract prend des wei en entrée :
amount = w3.toWei(amount, 'ether')

#Uniswap v2 prend des WETH au lieu des ETH dans les pools, 
# on a donc besoin de l'adresse du contract WETH :
weth_address = uniRouter.functions.WETH().call()

#Les adresses pour la pair que l'on souhaite swap : ETH->DAI (donc addresses WETH, DAI)
path = [weth_address, dai_address]

output = uniRouter.functions.getAmountsOut(amount, path).call()

print(output)

amountOutMin = output[-1]

print(w3.fromWei(amountOutMin, 'ether'))



# Swap : 

# parce que le calcul ne marche pas dans pour cette fonction
gas = 160000

tx_dict = uniRouter.functions.swapExactETHForTokens(
    amountOutMin, path, metaAccount.address, int(time.time())+10*60).buildTransaction({
        'from': metaAccount.address,
        'nonce': w3.eth.getTransactionCount(metaAccount.address),
        'value': amount,
        'gas' : gas,
        'gasPrice': w3.eth.gasPrice
    }
)
tx = w3.eth.account.signTransaction(tx_dict, metaAccount.key)
result = w3.eth.sendRawTransaction(tx.rawTransaction)
print(result.hex())

