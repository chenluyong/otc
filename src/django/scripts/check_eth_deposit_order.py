
import requests,json,math

# sys.path.append("F:\\projects\\2020\\we\\coin_switch.git\\src\\django\\scripts\\explorer")
from explorer import esplora


ex = esplora.esplora()


def get_block_height():
    return requests.get("http://btcexplorer.eshanren.com/api/blocks/tip/height").text


def get_user_deposit_order(page:int,size:int):
    return [
        {
            "address":"1C1Vto3MBLGVBxoEUNCadA7abrA4jdY1VC"
        }
    ]
def get_user_child_deposit_order(page:int, size:int):
    return [
        {
            "address":"1C1Vto3MBLGVBxoEUNCadA7abrA4jdY1VC",
            "txid" : "0xf4f369ed853e9bbd74ff5a963e9e110b77ab14fe21eec30509481a6f655f0b1f"
        }
    ]

def get_user_deposit_order_count():
    return 1

def get_user_child_deposit_order_count():
    return 1


def push_user_child_deposit_order(order:dict):
    pass

def update_deposit_order_to_finished(txid:str):
    pass

PAGE_SIZE = 20

def check_deposit_order():

    # 获取监控地址列表
    order_count = get_user_deposit_order_count()

    page = math.ceil(order_count / PAGE_SIZE)
    for p in range(page):
        # 获取监控的地址列表
        orders = get_user_deposit_order(p, PAGE_SIZE)


        for o in orders:
            address = o['address']
            # 查余额
            # 查交易记录
            confirmed = True
            if confirmed:
                push_user_child_deposit_order(o)

def check_deposit_order_is_finished():
    # 获取监控地址列表
    order_count = get_user_child_deposit_order_count()

    page = math.ceil(order_count / PAGE_SIZE)
    for p in range(page):
        # 获取监控的地址列表
        orders = get_user_child_deposit_order(p, PAGE_SIZE)

        for o in orders:
            txid = o['txid']
            block_height = o['block_height']
            confirmed = True

            if not confirmed:
                update_deposit_order_to_finished('')

check_deposit_order()