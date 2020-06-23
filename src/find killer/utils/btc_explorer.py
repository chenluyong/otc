from abc import abstractmethod


class ExplorerAbstract:
    # def __init__(self,):

    @abstractmethod
    def get_transactions(self,_address):
        pass

    @abstractmethod
    def get_token_transactions(self,_address,token = None):
        pass

    @abstractmethod
    def get_transaction_detail(self,_txid):
        pass

    @abstractmethod
    def get_address_info(self, _address):
        pass

    @abstractmethod
    def get_address_balance(self,_address):
        pass

    @abstractmethod
    def get_address_spent_count(self,_address):
        pass

    @abstractmethod
    def broadcast(self,info):
        pass

class ExplorerRequestConstructor:
    pass

class ExplorerResponseInterpreter:
    pass



class Explorer(ExplorerAbstract):

    class inline_interpreter:
        def __init__(self, _url):
            self.base_url = _url
            self.block_end_points = {
                'block_info': '/block/',  # Returns information about a block. Requires block hash as data.
                'block_height': '/block-height/',  # Returns the hash of the block currently at height
                'last_block_height': "/blocks/tip/height",  # Returns the height of the last block.
                'last_block_hash': '/blocks/tip/hash',  # Returns the hash of the last block.
                'block_hash': '/block-height/',  # Returns the height of the last block.
                'ten_block_info': '/blocks/',  # Returns the 10 newest blocks starting at the tip or at start_height if specified.
                'transaction':'/address/',
            }

        def get_url(self,method,*args):
            return self.base_url + self.block_end_points.get(endpoint)

        def address_info(self, _address, _balance = None, _spent_count = None):
            json = {}
            if _address: json['address'] = _address
            if _balance: json['balance'] = _balance
            if _spent_count : json['spent_count'] = _spent_count
            return json

    def __init__(self, _url, _constructor, _interpreter):
        self.interpreter = self.inline_interpreter(_url)
        self.url = _url


    def _request(self, _url):
        pass
    #
    # def get_address_balance(self,_address):
    #     url = self.interpreter.get_url('balance',_address)
    #     response = self._request(url)
    #     return self.interpreter.get_address_balance(response)
    #
    # def get_transactions(self,_address):
    #     url = self.constructor.get_transactions_url(_address)
    #     response = self._request(url)
    #     return self.interpreter.get_transactions(response)
    #
    # def get_token_transactions(self,_address,token = None):
    #     url = self.constructor.get_token_transactions_url(_address,token)
    #     response = self._request(url)
    #     return self.interpreter.get_token_transactions(response)
    #
    # def get_transaction_detail(self,_txid):
    #     url = self.constructor.get_transaction_detail_url(_txid)
    #     response = self._request(url)
    #     return self.interpreter.get_transaction_detail(response)
    #
    # @abstractmethod
    # def get_address_info(self, _address):
    #     url = self.constructor.get_address_info_url(_address)
    #     response = self._request(url)
    #     return self.interpreter.get_address_info(response)

    @abstractmethod
    def get_address_balance(self,_address):
        pass

    @abstractmethod
    def get_address_spent_count(self,_address):
        pass

    @abstractmethod
    def broadcast(self,info):
        pass


class BTCExplorer(ExplorerAbstract):

    @abstractmethod
    def get_utxo(self,_address):
        pass

