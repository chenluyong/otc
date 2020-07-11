

from jsonrpc.exceptions import JSONRPCDispatchException,JSONRPCError

# balance not enough
class BalanceException(JSONRPCDispatchException):

    """ JSON-RPC Dispatch Exception.

    Should be thrown in dispatch methods.

    """
    CODE = 32000
    MESSAGE = 'balance error'

    def __init__(self, data=None, code=None, message=None,):
        self.code = getattr(self.__class__, "CODE", code)
        self.message = getattr(self.__class__, "MESSAGE", message)
        self.data = data
        self.error = JSONRPCError(code=self.code, message=self.message,data=self.data)

    def _setting(self, code, message):
        self.code = code
        self.message = message
        self.error = JSONRPCError(code=self.code, message=self.message,data=self.data)
        return self

    # 金额不足以扣除
    @property
    def BALANCE_NOT_ENOUGH(self):
        return self._setting(32001, "Balance not enough.")

    # 冻结的金额不足以扣除
    @property
    def FREEZE_BALANCE_NOT_ENOUGH(self):
        return self._setting(32002, "Freeze balance not enough.")

    # 更新余额，值为0
    @property
    def CHANGE_ERROR(self):
        return self._setting(32003, "Balance change error.")

    # 不支持的币种
    @property
    def COIN_NOT_SUPPORT(self):
        return self._setting(32004, "The coin is not supported.")

    # 重复提交
    @property
    def DUPLICATE_SUBMISSION(self):
        return self._setting(32005, "Duplicate submission.")