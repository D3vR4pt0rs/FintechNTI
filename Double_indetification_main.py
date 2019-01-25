from py_ecc import secp256k1
from web3 import Web3
web3=Web3(Web3.HTTPProvider('https://sokol.poa.network'))

uuid="e40989524e3f46a4894d4460fac60251"
pin_code="3735"

def generate_private_key(uuid,pin_code):
    privateKey=web3.sha3(web3.sha3(web3.sha3(web3.sha3(web3.sha3(text='')+int(uuid,16).to_bytes(16, 'big')+int(pin_code[0],16).to_bytes(1, 'big'))+int(uuid,16).to_bytes(16, 'big')+int(pin_code[1],16).to_bytes(1, 'big'))+int(uuid,16).to_bytes(16, 'big')+int(pin_code[2],16).to_bytes(1, 'big'))+int(uuid,16).to_bytes(16, 'big')+int(pin_code[3],16).to_bytes(1, 'big')).hex()
    return privateKey

def privToPub(priv):
     priv = int(priv, 16).to_bytes(32, 'big')
     res = secp256k1.privtopub(priv)
     x = res[0].to_bytes(32, 'big')
     y = res[1].to_bytes(32, 'big')
     return x+y

def pubToAddr(pub):
     return web3.sha3(pub).hex()[24:]

def privToAddr(priv):
    return pubToAddr(privToPub(priv))

print(web3.sha3(text='')+int(uuid, 16).to_bytes(16, 'big')+int(pin_code[0], 16).to_bytes(1, 'big'))
private=generate_private_key(uuid,pin_code)
public=privToPub(private)
addr=pubToAddr(public)
addrlast="0x"+addr[len(addr)-40:]

def getBalance(addr):
    balance=web3.eth.getBalance(Web3.toChecksumAddress(addr))
    return balance
balance=getBalance(addrlast)
print(balance)
