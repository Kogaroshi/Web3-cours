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

amount = w3.toWei(20, 'ether')

weth_address = uniRouter.functions.WETH().call()

#Les adresses pour la pair que l'on souhaite swap : DAI->ETH
path = [dai_address, weth_address]
output = uniRouter.functions.getAmountsOut(amount, path).call()

print(output)
amountOutMin = output[-1]
print(w3.fromWei(amountOutMin, 'ether'))


# DAI contract

with open("./contracts/abi/erc20_abi.json") as f:
    dai_abi = json.load(f)
dai_contract = w3.eth.contract(
    address= dai_address,
    abi= dai_abi
)

#Approve ERC20 transfer

approve_tx_dict = dai_contract.functions.approve(
    uniswap_router2_address, amount).buildTransaction({
        'from': metaAccount.address,
        'nonce': w3.eth.getTransactionCount(metaAccount.address)
    }
)
approve_tx = w3.eth.account.signTransaction(approve_tx_dict, metaAccount.key)
approve_result = w3.eth.sendRawTransaction(approve_tx.rawTransaction)
print(approve_result.hex())
approve_txReceipt = w3.eth.waitForTransactionReceipt(approve_result)

print(approve_txReceipt['status'])

# Swap : 

# parce que le calcul ne marche pas dans pour cette fonction
gas = 160000

tx_dict = uniRouter.functions.swapExactTokensForETH(
    amount, amountOutMin, path, metaAccount.address, int(time.time())+10*60).buildTransaction({
        'from': metaAccount.address,
        'nonce': w3.eth.getTransactionCount(metaAccount.address),
        'value': 0,
        'gas' : gas,
        'gasPrice': w3.eth.gasPrice
    }
)
tx = w3.eth.account.signTransaction(tx_dict, metaAccount.key)
result = w3.eth.sendRawTransaction(tx.rawTransaction)
print(result.hex())

