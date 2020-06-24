
import requests,json

class btc:
    # 地址信息：https://explorer-web.api.btc.com/v1/eth/accounts/0xfdb16996831753d5331ff813c29a93c76834a0ad
    # 代币列表：https://explorer-web.api.btc.com/v1/eth/accounts/0xfdb16996831753d5331ff813c29a93c76834a0ad/tokens?size=25&page=1&type=1
    # type： 是否隐藏币价为0的代币
    # 交易记录：https://explorer-web.api.btc.com/v1/eth/accounts/0xfdb16996831753d5331ff813c29a93c76834a0ad/txns?page=1&size=25
    # 代币交易记录：https://explorer-web.api.btc.com/v1/eth/accounts/0xfdb16996831753d5331ff813c29a93c76834a0ad/tokentxns?page=3&size=25
    # 交易详情：
    # 1. https://explorer-web.api.btc.com/v1/eth/txns/0xa3528e4a9444a30c38337156a528d7825ea1a45b09d398d27a74135665ca8278
    # 2. https://explorer-web.api.btc.com/v1/eth/internaltxns/0xa3528e4a9444a30c38337156a528d7825ea1a45b09d398d27a74135665ca8278?limit=5
    # 3. https://explorer-web.api.btc.com/v1/eth/tokentxns/0xa3528e4a9444a30c38337156a528d7825ea1a45b09d398d27a74135665ca8278?page=1&size=5
    block_end_points = {
        'tx': '/txns/{0}',
        'txs': '/accounts/{0}/txns?page={1}&size={2}',
        'txs_token': '',
        'txs_tokens': '/accounts/{0}/tokentxns?page={1}&size={2}',
        'address': '/accounts/{0}',
        'address_token': '',
        'address_tokens':'/accounts/{0}/tokens?page={1}&size={2}&type={3}',

    }
    base_url = "https://explorer-web.api.btc.com/v1/eth"
    precision = 10 ** 18


    def call(self,method, *args):
        url = self.base_url + self.block_end_points.get(method)
        url = url.format(*args)
        response = requests.get(url).text
        response_json = json.loads(response)
        return self.interpreter(method, response_json)

    def interpreter(self, method, _json):
        pass