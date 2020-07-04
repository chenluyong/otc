

HTTP_CODE_SUCCESS = '200'
HTTP_CODE_BAD_REQUEST = '400'
HTTP_CODE_UNAUTHORIZED = '401'
HTTP_CODE_FORBIDDEN = '403'
HTTP_CODE_NOT_FOUND = '404'
HTTP_CODE_INTERNAL_SERVER_ERROR = '500'
HTTP_CODE_STD_MAX_LIMIT = '600'

# 自定义错误 10000 - 19999
HTTP_CODE_CUSTOM_START = '10000'
HTTP_CODE_INCORRECT_PASSWORD = '40101'
HTTP_CODE_ERROR = '50001'
HTTP_CODE_CUSTOM_END = '60000'


http_code_cn = {
    # 200 - 299
    HTTP_CODE_SUCCESS : '成功',

    # 400 - 499
    HTTP_CODE_BAD_REQUEST : '请求参数错误',
    HTTP_CODE_UNAUTHORIZED : '无权限访问',
    HTTP_CODE_FORBIDDEN : '无权限访问',
    HTTP_CODE_NOT_FOUND : '未找到',

    # 500 - 599
    HTTP_CODE_INTERNAL_SERVER_ERROR : '系统内部错误',

    # 自定义错误 10000 - 19999
    HTTP_CODE_INCORRECT_PASSWORD : '账号或密码错误',
    HTTP_CODE_ERROR : '未知错误码',
}
http_code_en = {

}


def get_default_http_code():
    return HTTP_CODE_SUCCESS

def get_http_code(code, language = 'zh'):

    http_code_text = http_code_cn.copy()

    if code not in http_code_text:
        response = http_code_text.get(HTTP_CODE_ERROR)
    else:
        response = http_code_text.get(code)

    return (int(code), response)