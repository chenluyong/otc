

import requests,json
#
class ETHExplorer:
    block_end_points = {
        'txs': '/accounts/{0}/txns?page={1}&size={2}',
        'tx': '/tx/{0}',
        'address': '/accounts/{0}'
    }

    base_url = "https://explorer-web.api.btc.com/v1/eth"
    precision = 10 ** 18

    def call(self, method, *args):
        url = self.base_url + self.block_end_points.get(method)
        url = url.format(*args)
        response = requests.get(url).text
        response_json = json.loads(response)
        return self.interpreter(method, response_json)

    def interpreter(self, method, _json):
        ret_json = {}
        if method == 'address':
            ret_json = self.__address(_json)
        elif method == 'txs':
            ret_json = self.txs(_json)
        elif method == 'tx':
            ret_json = self.tx(_json)
        return ret_json


    def __value(self, value, precision = 8):
        v = 0
        if type(value) == type('str'):
            v = float(value)

        if v == 0 or v == None:
            return 0

        return round(v,precision)

    def tx(self, _tx):
        is_token = False
        token_detail = {
        }
        to = _tx['receiver_hash']

        if _tx['receiver_type'] == 1:
            is_token = True
            token_detail = {
                # 'token_symbol' : 'USDT',
                'token_name' : _tx['receiver_name']
            }
        ret = {
            'txid':_tx['tx_hash'],
            'from':_tx['sender_hash'],
            'from_size':1,
            # 'from_detail':None,
            'to':_tx['receiver_hash'],
            'to_size': 1,
            # 'to_detail': None,
            'value':self.__value(_tx['amount'], 8),
            'fee':self.__value((_tx['fee']),8),
            # 'fee_detail':{
            #     'gas_price' : None,#self.value(fee / _tx['size'],10),
            #     'gas_used' : None,#_tx['size']
            # },
            'status':{
                'confirmed' : True if _tx['status'] == 'success' else False,
                'block_height' : _tx['block_height'],
                'block_hash': None,
                'block_time':_tx['created_ts']
            },
            'is_token':is_token,
            # 'token_detail' : {
            #     'token_name' : None,
            #     'token_symbol' : None,
            #     'from' : None,
            #     'to' : None,
            #     'value' : None
            # }
        }
        if is_token:
            ret ['token_detail'] = token_detail

        return ret

    def __address(self, cjson):
        data = cjson['data']
        address = data['account_hash']
        balance = float(data['balance_eth'])
        return {
            'address':address,
            'balance':round(balance,8),
            'tx_count':data['total_tx'],
            'address_alias':data['name']
        }


    def txs(self, _json):
        txs = _json['data']['list']

        ret_json = []
        for _tx in txs:
            tx = self.tx(_tx)
            ## 其它
            ret_json.append(tx)
        return ret_json
