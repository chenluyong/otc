import hashlib


def get_address(coin_name,pos):
    pos = coin_name + str(pos)
    hash = hashlib.sha256(pos.encode('utf8'))
    return '0x' + hash.hexdigest()[0:40]

