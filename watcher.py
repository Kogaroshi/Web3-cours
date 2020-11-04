from common import w3, metaAccount, postit_address
import json
import time
from os import system
from web3.logs import STRICT, IGNORE, DISCARD, WARN
from pprint import pprint



with open("./contracts/abi/post-it-abi.json") as f:
    postit_abi = json.load(f)

postIt = w3.eth.contract(
    address = postit_address,
    abi = postit_abi
)

#To test : 

address_list = []

incomeFilter = w3.eth.filter('latest')
while(True):
    filterLogs = w3.eth.getFilterChanges(incomeFilter.filter_id)
    blocks = [w3.eth.getBlock(l, True) for l in filterLogs]
    if(len(blocks) > 0):
        for b in blocks:
            txs = b['transactions']
            for t in txs :
                receipt = w3.eth.getTransactionReceipt(t['hash'])
                txLogs = receipt['logs']
                for l in txLogs:
                    if(l['topics'][0].hex() == '0x476e04c786e60f629af918e59f7b2d948f3b488bf1258cab1bf3a4351521b46f'):
                        if(l['address'] != postit_address and l['address'] not in address_list):
                            address_list.append(l['address'])
    system('clear')
    #print contracts
    for a in address_list:
        tempContract = w3.eth.contract(
            address = a,
            abi = postit_abi
        )
        print("Contract at " + a)
        print("Message :  " + tempContract.functions.getMessage().call())
    time.sleep(5)
