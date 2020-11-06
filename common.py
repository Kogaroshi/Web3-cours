from web3 import Web3, HTTPProvider
import sys
import os
import json
import time
from pprint import pprint

w3 = Web3(HTTPProvider("http://37.187.153.186:8554",request_kwargs={'timeout':60}))

#--------- Create account ------------

#account = w3.eth.account.create('BTRE1B45T1B4TG6ZBTZ641BTRZ6TBERZ6Z')
#print(account.address)
#print(account.key)
#pprint(w3.eth.account.encrypt(account.key, 'password'))

#---------------------------------------

#---------Load local account-------------

with open('./account/encrypted_key.json') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, 'password')
localAccount = w3.eth.account.from_key(private_key)

#---------------------------------------

#---------Load Metamask account-------------

#export METAKEY='key'
metaKey = os.environ['METAKEY'] #Add the new account key
metaAccount = w3.eth.account.from_key(metaKey)

#---------------------------------------

uniswap_router2_address = Web3.toChecksumAddress("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")

dai_address = Web3.toChecksumAddress("0x4F96Fe3b7A6Cf9725f59d353F723c1bDb64CA6Aa")

postit_address = Web3.toChecksumAddress("0x8A488071D7456ebab56a9700b980A4a628F9FBB0")