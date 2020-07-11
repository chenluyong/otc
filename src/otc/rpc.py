
from jsonrpc.backend.django import api



@api.dispatcher.add_method(name="my.method")
def my_method(request, *args, **kwargs):
    # rsp = Test().get(request,args,kwargs)
    # print(rsp.data)

    return args, kwargs#,rsp.data