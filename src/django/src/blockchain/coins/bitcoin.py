import requests
import json

class CoinBase:


    # def address(self,address):
    #     pass

    def is_address(self,address):
        # print(__class__,":is_address")
        pass

class Bitcoin(CoinBase):
    url = "http://btcexplorer.eshanren.com/api"
    address = ""
    def __init__(self, _address):
        self.address = _address

    def info(self, _realtime = False):
        res = requests.get(self.url + "/address/" + self.address).text
        res_json = json.loads(res)
        address_info = res_json['chain_stats']

        # 实时
        if _realtime:
            memory_address_info = res_json['mempool_stats']
            address_info['funded_txo_count'] += memory_address_info['funded_txo_count']
            address_info['funded_txo_sum'] += memory_address_info['funded_txo_sum']
            address_info['spent_txo_count'] += memory_address_info['spent_txo_count']
            address_info['spent_txo_sum'] += memory_address_info['spent_txo_sum']
            address_info['tx_count'] += memory_address_info['tx_count']

        balance = address_info['funded_txo_sum'] - address_info['spent_txo_sum']
        spent_count = address_info['spent_txo_count']
        ret = {
            "address" : self.address,
            "balance" : balance,
            "spent_count": spent_count,
        }
        return ret

    def utxo(self, _realtime = False):
        request_url = self.url + "/address/" + self.address + "/utxo"
        res = requests.get(request_url).text
        res_json = json.loads(res)
        print(_realtime)
        # 实时(含内存池)
        if _realtime:
            return res_json

        # 确认
        data = []
        for item in res_json:
            if item['status']['confirmed']:
                data.append(item)
        return data

    def transaction(self, _realtime = False):
        request_url = self.url + "/address/" + self.address + "/txs"
        # 确认
        if _realtime != False:
            request_url += "/chain"

        res = requests.get(request_url).text
        res_json = json.loads(res)


        return res_json

# b = Bitcoin("3KWoFdjEjKAGXr4aiqWzBd8cPRXTX5SkMt")
# print(b.transaction(1))
