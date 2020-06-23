import requests
import json
from time import sleep
import time
# from .btc_explorer import BTCExplorer
# https://python.gotrained.com/python-json-api-tutorial/
# https://github.com/Blockstream/esplora/blob/master/API.md

class esplora:
    block_end_points = {
        'block_info': '/block/',  # Returns information about a block. Requires block hash as data.
        'block_height': '/block-height/',  # Returns the hash of the block currently at height
        'last_block_height': "/blocks/tip/height",  # Returns the height of the last block.
        'last_block_hash': '/blocks/tip/hash',  # Returns the hash of the last block.
        'block_hash': '/block-height/',  # Returns the height of the last block.
        'ten_block_info': '/blocks/',
    # Returns the 10 newest blocks starting at the tip or at start_height if specified.
        'txs': '/address/{0}/txs',
        'tx': '/tx/{0}',
        'utxo':'/address/{0}/utxo',
        'address': '/address/{0}'

    }
    base_url = "http://btcexplorer.eshanren.com/api"
    precision = 10 ** 8

    def call(self,method, *args):
        url = self.base_url + self.block_end_points.get(method)
        url = url.format(*args)
        response = requests.get(url).text
        response_json = json.loads(response)
        return self.interpreter(method, response_json)

    def interpreter(self,method, _json):
        ret_json = {}
        if method == 'address':
            chain_stats = _json.get('chain_stats')
            ret_json['address'] = _json.get('address')
            ret_json['balance'] = (chain_stats.get('funded_txo_sum') - chain_stats.get('spent_txo_sum')) / self.precision
            ret_json['spent_count'] = chain_stats.get('spent_txo_count')
        elif method == 'txs':
            ret_json = self.txs(_json)
        return json.dumps(ret_json)

    def value(self,value):
        ret_value = value / self.precision
        return round(ret_value,8)

    def tx(self, _tx):
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
        print(fee)
        tx['fee'] = self.value(fee)

        tx['fee_detail'] = {
            'gas_price': round(fee / gas_used, 10),
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

print(esplora().call('address', '1P5ebVoi3J4KQJyQbwPmDzJtGm4jyC1rMh'))
print(esplora().call('txs', '1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY'))
print(esplora().call('tx', 'b3060c0e237baf0486d6b5d99c8edf13ccf8933373116380c96950c219e8ee33'))
print(esplora().call('utxo', '1P5ebVoi3J4KQJyQbwPmDzJtGm4jyC1rMh'))

# class esplora(BTCExplorer):
#
#     pass
#
#     def get_transaction(self,_address):
#         self.endpoint_chooser('transaction',_address + '/txs')
#
#     base_url = "http://btcexplorer.eshanren.com/api"
#
#     # end points to get data from blocks
#     block_end_points = {
#         'block_info': '/block/',  # Returns information about a block. Requires block hash as data.
#         'block_height': '/block-height/',  # Returns the hash of the block currently at height
#         'last_block_height': "/blocks/tip/height",  # Returns the height of the last block.
#         'last_block_hash': '/blocks/tip/hash',  # Returns the hash of the last block.
#         'block_hash': '/block-height/',  # Returns the height of the last block.
#         'ten_block_info': '/blocks/',  # Returns the 10 newest blocks starting at the tip or at start_height if specified.
#         'transaction':'/address/',
#     }
#
#     def tx(self):
#         pass
#
#     def endpoint_chooser(self, endpoint, data=''):
#         if data is None:
#             return self.base_url + self.block_end_points.get(endpoint)
#         else:
#             return self.base_url + self.block_end_points.get(endpoint) + str(data)
#
#
#     def last_block_height(self):
#         last_block_height_url = self.endpoint_chooser('last_block_height')
#         last_block_height_request = requests.get(last_block_height_url)
#         last_block_height = last_block_height_request.text
#         return last_block_height
#
#
#     # gets the height of the last block and returns the block hash
#     def last_block_height_and_hash(self):
#         # gets the height of last block
#         last_block_height_url = self.endpoint_chooser('last_block_height')
#         last_block_height_request = requests.get(last_block_height_url)
#         last_block_height = last_block_height_request.text
#
#         # last block hash
#         last_block_hash_url = self.endpoint_chooser('block_hash', last_block_height)
#         last_block_hash_request = requests.get(last_block_hash_url)
#         last_block_hash = last_block_hash_request.text
#         return last_block_hash
#
#
#     # takes the hash of a block and returns that block's info as json
#     def get_block_info(self,block_hash_info):
#         # last block info
#         block_info_url = self.endpoint_chooser('block_info', block_hash_info)
#         block_info_request = requests.get(block_info_url)
#         block_info = block_info_request.text
#         parsed_block_info = json.loads(block_info)
#         return (json.dumps(parsed_block_info, indent=4))
#
#
#     # last block status
#     def get_block_status(self):
#         block_status_url = block_info_url + '/status'
#         block_status_request = requests.get(block_status_url)
#         block_status = block_status_request.text
#         parsed_block_status = json.loads(block_status)
#         print('block status is: ' + str(parsed_block_status.get('in_best_chain')))
#
#
#     # returns a block transaction list
#     def block_txs(self):
#         block_txs_url = block_info_url + '/txs'
#         block_txs_request = requests.get(block_txs_url)
#         block_txs = block_txs_request.text
#         parsed_block_txs = json.loads(block_txs)
#         json_block_txs = json.dumps(parsed_block_txs, indent=4)
#         return json_block_txs
#
#
#     # returns a list of ids from every transaction in a block
#     def block_txs_id(self):
#         block_txs_id_url = block_info_url + '/txids'
#         block_txs_id_request = requests.get(block_txs_id_url)
#         block_txs_id = block_txs_id_request.text
#         parsed_block_txs_id = json.loads(block_txs_id)
#         json_block_txs_id = json.dumps(parsed_block_txs_id, indent=4)
#         return json_block_txs_id
#
#
#     # returns a list with info of the latest 10 blocks
#     def ten_block_info(self):
#         ten_block_info_url = self.endpoint_chooser('ten_block_info')
#         ten_block_info_request = requests.get(ten_block_info_url)
#         ten_block_info = ten_block_info_request.text
#         parsed_ten_block_info = json.loads(ten_block_info)
#         json_ten_block_info = json.dumps(parsed_ten_block_info, indent=4)
#         return json_ten_block_info
#
#
#     # gets information from a transaction's summary, inputs and outputs.
#     def tx_info(self, tx_id):
#         tx_info_url = self.base_url + '/tx/' + tx_id
#         tx_info_request = requests.get(tx_info_url)
#         tx_info = tx_info_request.text
#         if tx_info == 'Invalid hash string':
#             print('Transaction not found, please check the id and try again')
#         else:
#             parsed_tx_info = json.loads(tx_info)
#             txid = parsed_tx_info['txid']
#             tx_status = parsed_tx_info['status']['confirmed']
#             tx_block_height = parsed_tx_info['status']['block_height']
#             tx_block_hash = parsed_tx_info['status']['block_hash']
#             tx_block_time = parsed_tx_info['status']['block_time']
#             tx_block_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tx_block_time))
#             tx_confirmations = int(self.last_block_height()) - int(tx_block_height)
#             tx_fee = parsed_tx_info['fee']
#             tx_input_count = len(parsed_tx_info['vin'])
#             tx_output_count = len(parsed_tx_info['vout'])
#
#             print('-------------------------------------------------------------------------------')
#             print('-------------------------------------------------------------------------------')
#             print('TRANSACTION SUMMARY')
#             print('Transaction id: ' + str(txid))
#             print('Transaction confirmed: ' + str(tx_status))
#             print('Block height: ' + str(tx_block_height))
#             print('Block hash: ' + str(tx_block_hash))
#             print('Block time: ' + str(tx_block_time) + '(' + str(tx_block_date) + ')')
#             print('Number of confirmations: ' + str(tx_confirmations))
#             print('fee payed: ' + str(tx_fee) + ' sats (' + str(tx_fee / 100000000) + ' BTC)')
#             print('')
#             print('INPUT AND OUTPUT INFORMATION')
#
#             # inputs
#             print('NUMBER OF INPUTS: ' + str(tx_input_count))
#             # iterates over vin to extract the information on each input
#             i = 0
#             for inpt in parsed_tx_info['vin']:
#                 print(' Input #' + str(i))
#                 for key, value in inpt.items():
#                     if key == 'prevout':
#                         print('   Previous output data:')
#                         if parsed_tx_info['vin'][i]['is_coinbase'] == True:
#                             print('     This is a coninbase transaction. Coinbase transactions have no previous outputs')
#                         else:
#                             for item, value in parsed_tx_info['vin'][i]['prevout'].items():
#                                 if item == 'value':
#                                     print('    ' + str(item) + ': ' + str(value) + ' sats' + ' (' + str(
#                                         value / 100000000) + ' BTC)')
#                                 else:
#                                     print('    ' + str(item) + ': ' + str(value))
#                     else:
#                         print('   ' + str(key) + ': ' + str(value))
#                 i += 1
#
#             # outputs
#             print('NUMBER OF OUTPUTS: ' + str(tx_output_count))
#             # iterates over vout to extract the information on each output
#             i = 0
#             for output in parsed_tx_info['vout']:
#                 print(' Output #' + str(i))
#
#                 for key, value in output.items():
#                     if key == 'value':
#                         print('   ' + str(key) + ': ' + str(value) + ' sats' + ' (' + str(value / 100000000) + ' BTC)')
#                     else:
#                         print('   ' + str(key) + ': ' + str(value))
#
#                 # This code gets information about if the outputs in the tx have already been spent
#                 output_spends_url = tx_info_url + '/outspends'
#                 output_spends_request = requests.get(output_spends_url)
#                 output_spends = output_spends_request.text
#                 parsed_output_spends = json.loads(output_spends)
#
#                 for item, value in parsed_output_spends[i].items():
#                     if item == 'status':
#                         if parsed_output_spends[i]['status'] == None:
#                             print('   Status: NA')
#                         else:
#                             print('   Status:')
#                             for key, value in parsed_output_spends[i]['status'].items():
#                                 print('     ' + str(key) + ': ' + str(value))
#                     else:
#                         print('   ' + str(item) + ': ' + str(value))
#
#                 i += 1
#
#
#     # gets information from an address
#     def address_info(self):
#         while True:
#             try:
#                 user_address = input('Write the address you want to look for: ')
#                 address_info_url = self.base_url + '/address/' + user_address
#                 address_info_request = requests.get(address_info_url)
#                 address_info = address_info_request.text
#                 parsed_address_info = json.loads(address_info)
#                 json_address_info = json.dumps(parsed_address_info, indent=4)
#                 print(json_address_info)
#                 sleep(3)
#             except json.decoder.JSONDecodeError:
#                 print('Address not found, please try again')
#                 sleep(3)
#                 continue
#             else:
#                 break
#
#
#     # get mempool backlog statistics
#     def get_mempool(self):
#         mempool_url = self.base_url + '/mempool'
#         mempool_request = requests.get(mempool_url)
#         mempool = mempool_request.text
#         parsed_mempool = json.loads(mempool)
#
#         count = parsed_mempool['count']
#         vsize = parsed_mempool['vsize']
#         total_fee = parsed_mempool['total_fee']
#
#         print('-------------------------------------------------------------------------------')
#         print('MEMPOOL DATA')
#         print(' Number of transactions in the mempool: ' + str(count))
#         print(' Total size of the mempool: ' + str(vsize) + ' vbytes')
#         print(
#             ' Total fee paid by mempool transactions: ' + str(total_fee) + ' sats (' + str(total_fee / 100000000) + ' BTC)')
#
#         print(parsed_mempool['fee_histogram'][0][0])
#
#
#         # json_mempool = json.dumps(parsed_mempool, indent=4)
#         # print(json_mempool)
#
#
# # program code
#
# if '__main__' == __name__:
#     esplora = esplora()
#     program_running = True
#     while program_running:
#         print('-------------------------------------------------------------------------------')
#         print('YOUR OWN BITCOIN BLOCK EXPLORER')
#         print('Type any of the commands below to use the block explorer, then press enter.')
#         print('')
#         print(' LAST_BLOCK --> to see data from the latest block.')
#         print(' BLOCK      --> to choose a specific block height.')
#         print(' TX         --> to get the information from a transaction.')
#         print(' ADDRESS    --> to look for informtion about an address.')
#         print(' MEMPOOL    --> to get information about the current mempool.')
#         print(' X          --> to exit')
#         user_choice = input('What do you want to search for?: ').upper()
#         if user_choice == 'LAST_BLOCK':
#             block_hash_info = esplora.last_block_height_and_hash()
#             print(esplora.get_block_info(block_hash_info))
#             block_info_url = esplora.endpoint_chooser('block_info', block_hash_info)
#             esplora.get_block_status()
#             # print(block_txs_id())
#             # print(block_txs())
#         elif user_choice == 'BLOCK':
#             while True:
#                 try:
#                     user_block_height = input('Write the height or the hash of the block you want to search for: ')
#                     actual_block_height = int(esplora.last_block_height())
#                     int_user_block_height = int(user_block_height)
#                 except ValueError:
#                     print("Please enter numbers only")
#                     sleep(3)
#                     continue
#                 else:
#                     break
#             if int_user_block_height > actual_block_height or int_user_block_height < 0:
#                 print('Invalid block height, try again')
#                 sleep(3)
#             else:
#                 # block height. Returns the block hash
#                 block_hash_url = esplora.endpoint_chooser('block_height', user_block_height)
#                 block_hash_request = requests.get(block_hash_url)
#                 block_hash = block_hash_request.text
#                 print(esplora.get_block_info(block_hash))
#                 block_info_url = esplora.endpoint_chooser('block_info', block_hash)
#                 esplora.get_block_status()
#                 # print(block_txs_id())
#                 # print(block_txs())
#         elif user_choice == 'TX':
#             user_tx_id = input('Please write your transaction id: ')
#             esplora.tx_info(user_tx_id)
#             sleep(3)
#         elif user_choice == 'ADDRESS':
#             esplora.address_info()
#         elif user_choice == 'MEMPOOL':
#             esplora.get_mempool()
#             sleep(3)
#         elif user_choice == 'X':
#             print('goodbye!')
#             program_running = False
#         else:
#             print('You can only choose LAST_BLOCK, BLOCK, TX, ADDRESS, MEMPOOL or X, please try again')
#             sleep(3)