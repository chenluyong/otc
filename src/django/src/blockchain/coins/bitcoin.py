import requests
import json

class CoinBase:


    # def address(self,address):
    #     pass

    def is_address(self,address):
        # print(__class__,":is_address")
        pass

class BitcoinExplorer(CoinBase):
    url = "http://btcexplorer.eshanren.com/api"
    address = ""
    precision = 10 ** 8

    def __value(self, value, precision=8):
        ret_value = value / self.precision
        return round(ret_value, precision)


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
            "balance" : self.__value(balance),
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

class esplora:
    block_end_points = {
        # 'block_info': '/block/',  # Returns information about a block. Requires block hash as data.
        # 'block_height': '/block-height/',  # Returns the hash of the block currently at height
        # 'last_block_height': "/blocks/tip/height",  # Returns the height of the last block.
        # 'last_block_hash': '/blocks/tip/hash',  # Returns the hash of the last block.
        # 'block_hash': '/block-height/',  # Returns the height of the last block.
        # 'ten_block_info': '/blocks/',
        # Returns the 10 newest blocks starting at the tip or at start_height if specified.
        'txs': '/address/{0}/txs',
        'tx': '/tx/{0}',
        'utxo': '/address/{0}/utxo',
        'address': '/address/{0}'
    }

    base_url = "http://btcexplorer.eshanren.com/api"
    precision = 10 ** 8

    def call(self, method, *args):
        url = self.base_url + self.block_end_points.get(method)
        url = url.format(*args)
        response = requests.get(url).text
        response_json = json.loads(response)
        return self.interpreter(method, response_json)

    def interpreter(self, method, _json):
        ret_json = {}
        if method == 'address':
            chain_stats = _json.get('chain_stats')
            ret_json['address'] = _json.get('address')
            ret_json['balance'] = (chain_stats.get('funded_txo_sum') - chain_stats.get(
                'spent_txo_sum')) / self.precision
            ret_json['spent_count'] = chain_stats.get('spent_txo_count')

        elif method == 'txs':
            ret_json = self.txs(_json)
        elif method == 'tx':
            ret_json = self.tx(_json)
        elif method == 'utxo':
            ret_json = self.utxo(_json)
        return ret_json

    def value(self, value, precision=8):
        if value == None or value == 0 or value == "":
            return 0
        ret_value = value / self.precision
        return round(ret_value, precision)

    def tx(self, _tx):
        # vin vout 处理
        tx_from = 'multi-address'
        tx_from_detail = _tx['vin']
        vin_size = len(_tx['vin'])

        tx_to = 'multi-address'
        tx_to_detail = _tx['vout']
        vout_size = len(_tx['vout'])

        # 总转账金额
        transfer = 0

        fee = _tx['fee'] if _tx['fee'] != None else 0


        for pos in range(vin_size):
            if _tx['vin'][pos]['is_coinbase']:
                tx_from = 'coinbase'
                break
            # 换算 value
            prevout = _tx['vin'][pos]['prevout'].copy()
            value = self.value(prevout['value'])
            tx_from_detail[pos]['prevout']['value'] = value

            # 设置 from
            if vin_size == 1:
                tx_from = prevout['scriptpubkey_address']

        for pos in range(vout_size):
            # 换算 value
            vout = _tx['vout'][pos].copy()
            value = self.value(vout['value'])
            tx_to_detail[pos]['value'] = value

            # 设置 to
            if vout_size == 1:
                tx_to = vout['scriptpubkey_address']
            transfer = transfer + vout['value']

        return {
            'txid':_tx['txid'],
            'from':tx_from,
            'from_size':vin_size,
            'from_detail':tx_from_detail,
            'to':tx_to,
            'to_size': vout_size,
            'to_detail': tx_to_detail,
            'value':self.value(transfer),
            'fee': self.value(fee),
            'fee_detail':{
                'gas_price' : self.value(fee / _tx['size'],10),
                'gas_used' : _tx['size']
            },
            'status':_tx['status'],
            'is_token':False,
        }



    def tx_v1(self, _tx):
        tx = {}
        tx['txid'] = _tx['txid']
        tx['from_detail'] = _tx['vin']

        # 总转账金额
        transfer = 0
        # vin vout 处理
        tx['from'] = 'multi-address'
        vin_size = len(tx['from_detail'])
        for pos in range(vin_size):
            if _tx['vin'][pos]['is_coinbase']:
                tx['from'] = 'coinbase'
                break
            # 换算 value
            prevout = _tx['vin'][pos]['prevout'].copy()
            value = self.value(prevout['value'])
            tx['from_detail'][pos]['prevout']['value'] = value

            # 设置 from
            if vin_size == 1:
                tx['from'] = prevout['scriptpubkey_address']

        tx['to'] = 'multi-address'
        tx['to_detail'] = _tx['vout']
        vout_size = len(tx['to_detail'])
        for pos in range(vout_size):
            # 换算 value
            vout = _tx['vout'][pos].copy()
            value = self.value(vout['value'])
            tx['to_detail'][pos]['value'] = value

            # 设置 to
            if vout_size == 1:
                tx['to'] = vout['scriptpubkey_address']
            transfer = transfer + self.value(vout['value'])

        tx['value'] = round(transfer, 8)
        fee = _tx['fee']
        if fee == None:
            fee = 0
        gas_used = _tx['size']
        tx['fee'] = self.value(fee)

        tx['fee_detail'] = {
            'gas_price': self.value(fee / gas_used, 10),
            'gas_used': gas_used
        }
        tx['status'] = _tx['status'].copy()
        tx['is_token'] = False
        return tx

    def txs(self, _json):
        ret_json = []
        for _tx in _json:
            tx = self.tx(_tx)
            ## 其它
            ret_json.append(tx)
        return ret_json

    def utxo(self, _json):
        ret_json = _json.copy()
        utxo_size = len(_json)
        for pos in range(utxo_size):
            value = ret_json[pos]['value']
            ret_json[pos]['value'] = self.value(value)
        return _json
