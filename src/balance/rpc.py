
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

    balance = BalanceHistoryModel()
    balance._user_id = user_id
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
    return _freeze(user_id,coin_name,business, business_id, change, detail if detail else None)


def _freeze(user_id,coin_name,business, business_id, change, detail):
    balance = BalanceHistoryModel()
    balance._user_id = user_id
    balance.coin_name = coin_name
    balance.business = business
    balance.business_id = business_id
    balance._change = change
    balance.detail = detail

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

    if user_id != None or user_id != 0:
        raise BalanceException(_("user_id can't to be {0}").format(user_id)).PARAMETER_ERROR

    ret = {}
    for coin_name in app_settings.SUPPORT_ASSETS:
        balances = BalanceHistoryModel.objects.filter(user_id=user_id,coin_name = coin_name)[:1]

        if len(balances) != 0:
            ret[coin_name] = {
                'available': str(balances[0].balance),
                'freeze': str(balances[0].freeze_balance)
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
    from django.db.models import Q
    import time

    user_id = None
    coin_name = None
    business = None
    start_time = None
    end_time = None
    offset = 0
    limit = 25
    try:
        user_id = args[0]
        coin_name = args[1]
        business = args[2]
        start_time = args[3]
        end_time = args[4]

        if args[5]:
            offset = args[5]
        if args[6]:
            limit = args[6]

    except IndexError as e:
        pass

    con = Q()
    if user_id != None and user_id != 0:
        con.children.append(('user_id',user_id))
    else:
        raise BalanceException(_("user_id can't to be {0}").format(user_id)).PARAMETER_ERROR

    if coin_name != None:
        con.children.append(('coin_name', coin_name))
    if business != None:
        con.children.append(('business', business))

    if start_time != None and start_time != 0:
        con.children.append(('change_at__gt', start_time))
        if end_time == None or end_time == 0:
            end_time = time.time()
        con.children.append(('change_at__lt', end_time))

    result = BalanceHistoryModel.objects.filter(con)[offset:offset+limit]
    count = BalanceHistoryModel.objects.filter(con).count()
    ret = []
    for r in result:
        ret.append({
            'id':r.id,
            'coin_name':r.coin_name,
            'business':r.business,
            'change':r.change,
            'balance':r.balance,
            'freeze_balance':r.freeze_balance,
            'time':r.change_at,
            'detail':r.detail
        })

    return {
        "offset" : offset,
        "limit" : limit,
        "count" : count,
        "data" : ret
    }

# * method: `asset.list`
# * params: none
@api.dispatcher.add_method(name="asset.list")
def asset(request, *args, **kwargs):
    return [
        'ETH','USDT'
    ]

