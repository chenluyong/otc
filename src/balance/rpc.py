
import json
from django.utils.translation import gettext_lazy as _

from jsonrpc.backend.django import api
from balance.services import *
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
    slz = BalanceUpdateRequestSerializer(args,kwargs)
    return balance_update(slz.user_id,slz.coin_name,slz.business, slz.business_id, slz.change, json.loads(request.body))

# 冻结与解冻
@api.dispatcher.add_method(name="balance.freeze")
def freeze(request, *args, **kwargs):
    slz = BalanceUpdateRequestSerializer(args,kwargs)
    return freeze_balance_update(slz.user_id,slz.coin_name,slz.business, slz.business_id, slz.change, slz.detail if slz.detail else json.loads(request.body))


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
    user_id = None
    asset = None
    try:
        user_id = args[0]
        asset = args[1]
    except IndexError as e:
        pass

    if user_id is None or user_id == 0:
        raise BalanceException(_("user_id can't to be {0}").format(user_id)).PARAMETER_ERROR

    # 检测客户端是否指定查询
    assets = app_settings.SUPPORT_ASSETS
    if asset:
        if asset not in app_settings.SUPPORT_ASSETS:
            raise BalanceException(_("Not support the {0} coin").format(asset)).ASSET_NOT_SUPPORT
        else:
            assets = [asset]

    return balance_query(user_id, assets)


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
    slz = BalanceHistoryRequestSerializer(args)
    return balance_history(slz.user_id,slz.coin_name, slz.business, slz.start_time, slz.end_time, slz.offset, slz.limit)

# * method: `asset.list`
# * params: none
@api.dispatcher.add_method(name="asset.list")
def asset(request, *args, **kwargs):
    return app_settings.SUPPORT_ASSETS
