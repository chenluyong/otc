
from jsonrpc.backend.django import api




# 创建摊位
@api.dispatcher.add_method(name="market.create_booth")
def market_create_booth(request, *args, **kwargs):
    return args, kwargs#,rsp.data

# 市场摊位列表
@api.dispatcher.add_method(name="market.list")
def market_list(request, *args, **kwargs):
    return args, kwargs#,rsp.data




# * method: `order.put_market`
# * params:
# 1. user_id: user ID，Integer
# 2. market: market name，String
# 3. side: 1: sell, 2: buy，Integer
# 4. amount: count or amount，String
# 5. taker_fee_rate: taker fee
# 6. source: String, source，up to 30 bytes
# * result: order detail
# * error:
# 10. balance not enough
# * example:
# 自动市场价购买
@api.dispatcher.add_method(name="order.put_market")
def put_market(request, *args, **kwargs):
    return args, kwargs#,rsp.data


# 下单
@api.dispatcher.add_method(name="order.pact")
def pact(request, *args, **kwargs):
    return args, kwargs#,rsp.data

# **取消委托订单**
# * method: `order.cancel`
# * params:
# 1. user_id: user ID
# 2. market：market
# 3. order_id： order ID
# * result: order detail
# * error:
# 10. order not found
# 11. user not match
@api.dispatcher.add_method(name="order.cancel")
def cancel(request, *args, **kwargs):
    return args, kwargs#,rsp.data


# 订单记录
@api.dispatcher.add_method(name="order.history")
def history(request, *args, **kwargs):
    return args, kwargs#,rsp.data