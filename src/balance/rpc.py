
import json
from django.utils.translation import gettext_lazy as _

from jsonrpc.backend.django import api
from balance.models import History as BalanceHistoryModel
from balance import app_settings
from utils.error import BalanceException

# * method: `balance.update`
# * params:
# 1. user_id: user ID，Integer
# 2. asset: asset name，String
# 3. business: business type，String
# 4. business_id: business ID，Integer, but it will only succeed once with multiple operations of the same user_id, asset, business or business_id
# 5. change: balance change，String, negative numbers for deduction
# 6. detail: Json object，attached information
# * result: "success"
# * error code:
# 10. repeat update
# 11. balance not enough
@api.dispatcher.add_method(name="balance.update")
def update(request, *args, **kwargs):
    user_id,coin_name,business, business_id, change, detail= args

    if coin_name not in app_settings.SUPPORT_ASSETS:
        raise BalanceException(_("Not support the {0} coin").format(coin_name)).COIN_NOT_SUPPORT

    balance = BalanceHistoryModel()
    balance.user_id = user_id
    balance.coin_name = coin_name
    balance.business = business
    balance.business_id = business_id
    balance._change = change
    balance.detail = detail if detail else json.loads(request.body)


    return balance.update_balance()

# 冻结与解冻
@api.dispatcher.add_method(name="balance.freeze")
def freeze(request, *args, **kwargs):
    user_id,coin_name,business, business_id, change, detail= args

    if coin_name not in app_settings.SUPPORT_ASSETS:
        raise BalanceException(_("Not support the {0} coin").format(coin_name)).COIN_NOT_SUPPORT

    balance = BalanceHistoryModel()
    balance.user_id = user_id
    balance.coin_name = coin_name
    balance.business = business
    balance.business_id = business_id
    balance._change = change
    balance.detail = detail if detail else json.loads(request.body)

    return balance.update_freeze()



# * method: `balance.update`
# * params:
# 1. user_id: user ID，Integer
# 2. asset: asset name，String
# 3. business: business type，String
# 4. business_id: business ID，Integer, but it will only succeed once with multiple operations of the same user_id, asset, business or business_id
# 5. change: balance change，String, negative numbers for deduction
# 6. detail: Json object，attached information
# * result: "success"
# * error code:
# 10. repeat update
# 11. balance not enough
@api.dispatcher.add_method(name="balance.query")
def query(request, *args, **kwargs):
    user_id = args[0]
    ret = {}
    for coin_name in app_settings.ASSETS:
        balances = BalanceHistoryModel.objects.filter(user_id=user_id,coin_name = coin_name)[:1]
        if len(balances) != 0:
            ret[coin_name] = {
                'available': str(balances[0].balance)
            }

    return ret


# * method: `balance.history`
# * params:
# 1. user_id: user ID, Integer
# 2. asset: asset name，which can be null
# 3. business: business，which can be null，use ',' to separate types
# 3. start_time: start time，0 for unlimited，Integer
# 4. end_time: end time，0 for unlimited, Integer
# 5. offset: offset position，Integer
# 6. limit: count limit，Integer
@api.dispatcher.add_method(name="balance.history")
def history(request, *args, **kwargs):

    # user_id,coin_name,business,start_time, end_time,offset,limit = args

    rsp = {
        "offset": 0,
        "limit": 25,
        "records": [
            {
                "time": 1570871173,
                "asset": "USDT",
                "business": "deposit",
                "change": "1.00000000",
                "balance":"1.00000000",
                "detail": {"txid":"09a2d150b944059cd4524d269389bf7d78614abb722597c558fe97013f4beeb2"}
            },
            {
                "time": 1570871172,
                "asset": "BTC",
                "business": "withdraw",
                "change": "-0.50000000",
                "balance":"0.50000000",
                "detail": {"txid":"09a2d150b944059cd4524d269389bf7d78614abb722597c558fe97013f4beeb2"}
            },
            {
                "time": 1570871171,
                "asset": "BTC",
                "business": "deposit",
                "change": "1.00000000",
                "balance":"1.00000000",
                "detail": {"txid":"09a2d150b944059cd4524d269389bf7d78614abb722597c558fe97013f4beeb2"}
            }
        ]
    }

    return rsp

# * method: `asset.list`
# * params: none
@api.dispatcher.add_method(name="asset.list")
def asset(request, *args, **kwargs):
    return [
        'ETH','USDT'
    ]

