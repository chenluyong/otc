

class Blockchain:
    # 普通交易："https://api.blockchain.info/v2/eth/data/account/0xfdb16996831753d5331ff813c29a93c76834a0ad/transactions?page=0&size=200"
    # 内联转账："https://api.blockchain.info/v2/eth/data/account/0xfdb16996831753d5331ff813c29a93c76834a0ad/internalTransactions?page=0&size=200"
    # 币价：https://blockchain.info/ticker?base=ETH
    # https://blockchain.info/ticker?base=BTC
    block_end_points = {
        'txs': '/account/{0}/transactions?page={1}&size={2}',
        'tx': '/tx/{0}',
        'utxo':'/address/{0}/utxo',
        'address': '/address/{0}'
    }