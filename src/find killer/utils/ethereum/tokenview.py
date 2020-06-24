

# 未确认的交易记录：https://eth.tokenview.com/api/pending/ntx/eth/0xfdb16996831753d5331ff813c29a93c76834a0ad
# 已确认的交易记录：https://eth.tokenview.com/api/eth/address/normal/0xfdb16996831753d5331ff813c29a93c76834a0ad/2/20
# 特定代币转账记录：https://eth.tokenview.com/api/eth/address/tokentrans/0xfdb16996831753d5331ff813c29a93c76834a0ad/0xdac17f958d2ee523a2206206994597c13d831ec7/1/10
# 不限制代币转账  ：https://eth.tokenview.com/api/eth/address/tokentrans/0xfdb16996831753d5331ff813c29a93c76834a0ad/1/20
# 地址余额趋势：https://eth.tokenview.com/api/address/balancetrend/eth/0xfdb16996831753d5331ff813c29a93c76834a0ad
# 地址代币信息：https://eth.tokenview.com/api/eth/address/tokenbalance/0xfdb16996831753d5331ff813c29a93c76834a0ad
# 交易详情：https://eth.tokenview.com/api/eth/tx/10326381/84

class tokenview:
    base_url = "https://eth.tokenview.com/api/eth"
    precision = 10 ** 18
    block_end_points = {
        'tx': '/txns/{0}',
        'txs': '/accounts/{0}/txns?page={1}&size={2}',
        'txs_token': '',
        'txs_tokens': '/accounts/{0}/tokentxns?page={1}&size={2}',
        'address': '/accounts/{0}',
        'address_token': '',
        'address_tokens': '/accounts/{0}/tokens?page={1}&size={2}&type={3}',
    }