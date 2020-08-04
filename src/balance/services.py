from balance.serializers import *
from balance.models import History as BalanceHistoryModel


# 充值、提现
def balance_update(user_id,coin_name,business,business_id,change,detail):
    balance = BalanceHistoryModel()
    balance.user_id = user_id
    balance.coin_name = coin_name
    balance.business = business
    balance.business_id = business_id
    balance.change = change
    balance.detail = detail

    return balance.update_balance()




# 冻结、解冻、消费
def freeze_balance_update(user_id, coin_name, business, business_id, change, detail):
    balance = BalanceHistoryModel()
    balance.user_id = user_id
    balance.coin_name = coin_name
    balance.business = business
    balance.business_id = business_id
    balance.change = change
    balance.detail = detail

    return balance.update_freeze()


def balance_query(user_id, assets):
    ret = {}
    for asset in assets:
        balances = BalanceHistoryModel.objects.filter(user_id=user_id,coin_name = asset)[:1]

        if len(balances) != 0:
            ret[asset] = {
                'available': str(balances[0].balance),
                'freeze': str(balances[0].freeze_balance)
            }

    return ret


def balance_history(user_id, coin_name, business, start_time, end_time, offset, limit):

    from django.db.models import Q
    import time


    con = Q()

    con.children.append(('user_id',user_id))

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