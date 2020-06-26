
import requests,json,math

# sys.path.append("F:\\projects\\2020\\we\\coin_switch.git\\src\\django\\scripts\\explorer")
from explorer import esplora


ex = esplora.esplora()


def get_block_height():
    return requests.get("http://btcexplorer.eshanren.com/api/blocks/tip/height").text


def get_user_deposit_order(page,size):
    return [
        {
            "address":"1C1Vto3MBLGVBxoEUNCadA7abrA4jdY1VC"
        }
    ]

def get_user_deposit_order_count():
    return 1


def push_user_deposit_order(utxo):
    pass

PAGE_SIZE = 20

def check_deposit_order():
    # 获取区块高度
    cache_height = 1
    now_height = int(get_block_height())

    # 查看是否存在新的区块
    if cache_height < now_height:
        order_count = get_user_deposit_order_count()

        page = math.ceil(order_count / PAGE_SIZE)
        for p in range(page):
            # 获取监控的地址列表
            orders = get_user_deposit_order(p, PAGE_SIZE)

            # 循环查看区块高度，每出现一个区块，就查一次地址列表的交易记录情况。
            for o in orders:
                address = o['address']
                utxos = json.dumps(ex.call('utxo',address))
                for u in utxos:
                    confirmed = u['confirmed']
                    if confirmed:
                        push_user_deposit_order(u)

check_deposit_order()