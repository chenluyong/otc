# import requests, json
#
#
# def test_api(api, coin_name, cmp_data=None):
#     request_url = api
#     headers = {
#         'content-type': 'application/json'
#     }
#     try:
#         res = requests.get(request_url, timeout=3).text
#     except TimeoutError as e:
#         raise Exception('{}请求超时'.format(coin_name))
#
#     res_json = json.loads(res)
#     if "error" in res_json and res_json['error']:
#         e = "{}: 余额接口请求失败".format(coin_name)
#         raise Exception(e)
#
#     if type(cmp_data) == type({}):
#
#         for item in cmp_data:
#             if res_json['data'][item] != cmp_data[item]:
#                 e = "{0}: 请求错误, {1}期望值{2},实际值{3}".format(coin_name, item, cmp_data[item], res_json['data'][item])
#                 raise Exception(e)
#     elif type(cmp_data) == type([]):
#         cmp_data = cmp_data[0]
#         print(cmp_data)
#         for item in cmp_data:
#             print('-'*10)
#             print(cmp_data[item])
#             if res_json['data'][0][item] != cmp_data[item]:
#                 e = "{0}: 请求错误, {1}期望值{2},实际值{3}".format(coin_name, item, cmp_data[item], res_json['data'][0][item])
#                 print(e)
#                 raise Exception(e)
#     return "success"
#
#
# def dingding_robot(data):
#     webhook = "https://oapi.dingtalk.com/robot/send?access_token=e181c0f1188252609fc00438314aaba3f8d8765a0e4086afa8a5fe08df317433"
#     headers = {'content-type': 'application/json'}  # 请求头
#     r = requests.post(webhook, headers=headers, data=json.dumps(data))  # json.dumps()函数是将字典转化为字符串
#     r.encoding = 'utf-8'
#     return (r.text)
#
#
# apis = {
#     # 'eos': [
#     #     'http://api.bepal.pro/api/v3/pledge?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=27&account=aaaabbbbbb11',
#     #     {},
#     # ],
#     'gxc': [
#         'http://api.bepal.pro/api/v3/balance?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=35&address=wsoo5201',
#         {
#             "coinType": 'gxc',
#             'isToken': 0,
#             'address': 'wsoo5201'
#         },
#
#     ],
#     'btc': [
#         'http://api.bepal.pro/api/v3/addressTxs?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=2&address=1ACvMFS41GfmEp9oJeXia725yvBf1e2ouM&pageSize=1000',
#         {
#             "coinType": 'btc',
#             'isToken': 0,
#             'addrstr': '1ACvMFS41GfmEp9oJeXia725yvBf1e2ouM'
#         },
#     ],
#     # 'IOST_account':[
#     #     'http://api.bepal.pro/api/v3/account?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=40&key=ENdDzCx9tForTWxjfajADuTEbVpbGMD8f51eGf7mss5',
#     #     [
#     #         {
#     #             'creator':'bepaladmin'
#     #         }
#     #     ]
#     # ]
# }
#
# errors = []
# for coin_name in apis:
#     try:
#         test_api(apis[coin_name][0], coin_name, apis[coin_name][1])
#         # test_api('http://api.bepal.pro/api/v3/balance?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=35&address=wsoo5201','eos')
#     except TimeoutError as e:
#         errors.append('{}请求超时'.format(coin_name))
#     except Exception as e:
#         errors.append(e.__str__())
#
# # print('-'*10)
# if len(errors):
#     data = {
#         "msgtype": "text",
#         "text": {
#             'content': '结果是{}'.format(json.dumps(errors, ensure_ascii=False))
#         },
#         "at": {
#             "atMobiles": [],
#             "isAtAll": False
#         }
#     }
#     print(data)
#     print(dingding_robot(data))
#
#


from django.test import TestCase

# Create your tests here.
import requests, json


def test_api(api, coin_name, cmp_data=None):
    request_url = api
    headers = {
        'content-type': 'application/json'
    }
    try:
        res = requests.get(request_url, timeout=3).text
    except TimeoutError as e:
        raise Exception('{}请求超时'.format(coin_name))

    res_json = json.loads(res)
    if "error" in res_json and res_json['error']:
        e = "{}: 接口请求失败".format(coin_name)
        raise Exception(e)

    if type(cmp_data) == type({}):

        for item in cmp_data:
            if res_json['data'][item] != cmp_data[item]:
                e = "{0}: 请求错误, {1}期望值{2},实际值{3}".format(coin_name, item, cmp_data[item], res_json['data'][item])
                raise Exception(e)
    elif type(cmp_data) == type([]):
        cmp_data = cmp_data[0]
        # print(cmp_data)
        for item in cmp_data:
            # print('-'*10)
            # print(cmp_data[item])
            if res_json['data'][0][item] != cmp_data[item]:
                e = "{0}: 请求错误, {1}期望值{2},实际值{3}".format(coin_name, item, cmp_data[item], res_json['data'][0][item])
                # print(e)
                raise Exception(e)
    return "success"


def dingding_robot(data):
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=c86275b5c044d6ccd5f836d52dd8f2f761237b787fbd95417eca26ddc7d63edf"
    headers = {'content-type': 'application/json'}  # 请求头
    r = requests.post(webhook, headers=headers, data=json.dumps(data))  # json.dumps()函数是将字典转化为字符串
    r.encoding = 'utf-8'
    return (r.text)


apis = {
    # 'eos': [
    #     'http://api.bepal.pro/api/v3/pledge?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=27&account=aaaabbbbbb11',
    #     {},
    # ],
    'gxc余额接口': [
        'http://api.bepal.pro/api/v3/balance?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=35&address=wsoo5201',
        {
            "coinType": 'gxc',
            'isToken': 0,
            'address': 'wsoo5201'
        },

    ],
    'btc交易列表接口': [
        'http://api.bepal.pro/api/v3/addressTxs?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=2&address=1ACvMFS41GfmEp9oJeXia725yvBf1e2ouM&pageSize=1000',
        {
            "coinType": 'btc',
            'isToken': 0,
            'addrstr': '1ACvMFS41GfmEp9oJeXia725yvBf1e2ouM'
        },
    ],
    #  'Iost余额接口':[
    #     'http://api.bepal.pro/api/v3/balance?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=40&address=bepal12345',
    #     {
    #          "coinType": 'iost',
    #         'isToken': 0,
    #         'address': 'bepal12345'},
    # ],
    'eth余额接口':[
        'http://api.bepal.pro/api/v3/balance?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=5&address=0xc513398656ca324132250c650b93dd0ea51beee4',
        {
            "coinType": 'eth',
            'isToken': 0,
            'address': '0xc513398656ca324132250c650b93dd0ea51beee4'},
    ],
    'btm交易列表接口':[
        'http://api.bepal.pro/api/v3/addressTxs?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=32&address=bm1qemjqwn2mlx8rcshjs5ryhcs8dz8tfx3myva7u5&pageSize=1000',
        {
            "coinType": 'btm',
            'isToken': 0,
            'addrstr': 'bm1qemjqwn2mlx8rcshjs5ryhcs8dz8tfx3myva7u5'},
    ],
    'gxc账户名接口':[
        'http://api.bepal.pro/api/v3/account?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=35&key=GXC5vYtxgQPqRFNk6poWHYv6fSVL3zFGr5rKq77hKznHb7PbaMtmf',
        [
            {
                'registrar_name':'opengateway'
            },
        ],
    ],
    'IOST账户名接口':[
        'http://api.bepal.pro/api/v3/account?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=40&key=ENdDzCx9tForTWxjfajADuTEbVpbGMD8f51eGf7mss5',
        [
            {
                'creator':'bepaladmin'
            }
        ]
    ],
}

errors = []
for coin_name in apis:

    try:
        test_api(apis[coin_name][0], coin_name, apis[coin_name][1])
        # test_api('http://api.bepal.pro/api/v3/balance?sid=srkj_tester&appkey=1cfc087ad1847b37922f9ac73487bb47&coinIndex=35&address=wsoo5201','eos')
    except TimeoutError as e:
        errors.append('{}请求超时'.format(coin_name))
    except Exception as e:
        errors.append(coin_name + e.__str__())
        # print(coin_name)
        # print(errors)

# print('-'*10)
if len(errors):
    data = {
        "msgtype": "text",
        "text": {
            'content': '结果是{}'.format(json.dumps(errors, ensure_ascii=False))
        },
        "at": {
            "atMobiles": [''],
            "isAtAll": False
        }
    }
    print(dingding_robot(data))
