
from jsonrpc.backend.django import api


# 今日充提币情况
@api.dispatcher.add_method(name="atm.status_today")
def status_today(request, *args, **kwargs):
    coin_name = args[0]
    return {
        "deposit": "322927.83496872",
        "withdraw": "322927.83496872",
    }