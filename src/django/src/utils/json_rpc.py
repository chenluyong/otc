
import requests
import json,base64

class rpc(object):
    __rpc_url = 'https://blockchain.eshanren.com/api/bitcoin/'
    __rpc_user = 'root'
    __rpc_password = '123456'
    __rpc_port = '8332'
    __id_count = 0
    __heaers = {
        'User-Agent' : 'Private Proxy/1.0',
        'Content-Type': 'text/plain',
    }

    def __init__(self, method = None):
        self.__method = method
        authpair = self.__rpc_user.encode('utf-8') + b':' + self.__rpc_password.encode('utf-8')
        self.__auth_header = b'Basic ' + base64.b64encode(authpair)
        self.__heaers['Authorization'] = self.__auth_header



    def __call(self, *args):
        rpc.__id_count += 1
        body = {
            "jsonrpc": "1.0",
            "id": self.__id_count,
            "method": self.__method,
            "params": args
        }

        response = requests.post(self.__rpc_url, json.dumps(body), headers=self.__heaers).text
        response_json = json.loads(response)
        # logging.info('Call [{0}] method and get server response: {1}'.format(self.__method, json.dumps(response_json)))
        return response_json


    def __getattr__(self, name):
        self.__method = name
        return self.__call
