from django.utils.translation import gettext_lazy as _

from jsonrpc.exceptions import JSONRPCDispatchException,JSONRPCError

# balance not enough
class BalanceException(JSONRPCDispatchException):

    """ JSON-RPC Dispatch Exception.

    Should be thrown in dispatch methods.

    """
    CODE = 32000
    MESSAGE = _('balance error')

    def __init__(self, data=None):
        self.code = self.CODE
        self.message = self.MESSAGE
        self.data = data

    def _setting(self, code, message):
        self.code = int(code)
        self.message = str(message)
        self.error = JSONRPCError(code=self.code, message=self.message,data=self.data)
        return self

    # 金额不足以扣除
    @property
    def BALANCE_NOT_ENOUGH(self):
        return self._setting(32001, _("Balance not enough."))

    # 冻结的金额不足以扣除
    @property
    def FREEZE_BALANCE_NOT_ENOUGH(self):
        return self._setting(32002, _("Freeze balance not enough."))

    # 更新余额，值为0
    @property
    def CHANGE_ERROR(self):
        return self._setting(32003, _("Balance change error."))

    # 不支持的币种
    @property
    def COIN_NOT_SUPPORT(self):
        return self._setting(32004, _("The coin is not supported."))

    # 重复提交
    @property
    def DUPLICATE_SUBMISSION(self):
        return self._setting(32005, _("Duplicate submission."))