from django.db import models
from django.db.utils import IntegrityError
from django.utils.translation import gettext_lazy as _

# Create your models here.
from utils.error import BalanceException




# 总财务账单
class History(models.Model):
    id = models.AutoField(primary_key=True)

    user_id = models.IntegerField(verbose_name='用户编号')
    coin_name = models.CharField(max_length=32, verbose_name='币种名称')
    business = models.CharField(max_length=32, verbose_name='业务系统行为', help_text='使用/解冻/冻结/充值/提现')
    business_id = models.IntegerField(verbose_name='订单详情编号',help_text='业务订单编号，可用于业务系统查看订单详情')
    change = models.FloatField(verbose_name='变更金额')
    balance = models.FloatField(verbose_name='活跃余额')
    # 冻结资金，解冻资金，消费冻结资金
    freeze_balance = models.FloatField(verbose_name='不可用余额',default=0)
    prev_id = models.IntegerField(verbose_name='上一笔账单编号',unique=True,null=True)
    change_at = models.FloatField(verbose_name='变更时间')
    detail = models.TextField(verbose_name='更多信息{object}',help_text='商户信息，创建交易时传入的信息。对账使用，不脱敏	',null=True)


    def update_balance(self):
        balances = History.objects.filter(user_id=self.user_id, coin_name=self.coin_name)[:1]

        prev_id = None
        if len(balances) != 0:
            prev = balances[0]
            self.prev_id = prev.id

            self.balance = prev.balance + self.change
            if self.balance < 0 :
                raise BalanceException(_("balance: {0} {1}").format(prev.balance,prev.coin_name)).BALANCE_NOT_ENOUGH

        elif self.change < 0:
            raise BalanceException(_("balance:0 {0}").format(self.coin_name)).BALANCE_NOT_ENOUGH

        elif self.change > 0:
            self.balance = self.change


        import time
        self.change_at = time.time()
        try:
            return self.save()
        except IntegrityError as e:
            raise BalanceException(e.args).DUPLICATE_SUBMISSION

    def update_freeze(self):
        balances = History.objects.filter(user_id=self.user_id, coin_name=self.coin_name)[:1]

        if len(balances) != 0:
            prev = balances[0]
            self.balance = prev.balance
            self.freeze_balance = prev.freeze_balance
            self.prev_id = prev.id

            if self.change > 0:
                self.balance = prev.balance - self.change
                if self.balance < 0:
                    raise BalanceException(_("balance: {0} {1}").format(prev.balance,prev.coin_name)).BALANCE_NOT_ENOUGH
                self.freeze_balance = prev.freeze_balance + self.change

            elif self.change < 0:
                self.freeze_balance = prev.freeze_balance + self.change
                if self.freeze_balance < 0:
                    raise BalanceException(_("balance: {0} {1}").format(prev.freeze_balance,prev.coin_name)).FREEZE_BALANCE_NOT_ENOUGH
                self.balance = prev.balance - self.change

            import time
            self.change_at = time.time()

            try:
                return self.save()
            except IntegrityError as e:
                raise BalanceException(e.args).DUPLICATE_SUBMISSION

        raise BalanceException(_("balance:0 {0}").format(self.coin_name)).BALANCE_NOT_ENOUGH

    def expend_freeze(self):
        balances = History.objects.filter(user_id=self.user_id, coin_name=self.coin_name)[:1]

        if len(balances) != 0:
            prev = balances[0]

            self.balance = prev.balance
            self.freeze_balance = prev.freeze_balance
            self.prev_id = prev.id

            if self.change > 0:
                self.freeze_balance = prev.freeze_balance - self.change
                if self.freeze_balance < 0:
                    raise BalanceException(
                        _("balance: {0} {1}").format(prev.freeze_balance, prev.coin_name)).FREEZE_BALANCE_NOT_ENOUGH
                self.freeze_balance = prev.freeze_balance - self.change

            try:
                return self.save()
            except IntegrityError as e:
                raise BalanceException(e.args).DUPLICATE_SUBMISSION

        raise BalanceException(_("balance:0 {0}").format(self.coin_name)).FREEZE_BALANCE_NOT_ENOUGH

    class Meta:
        ordering = ['-change_at']
        index_together = [
            ('user_id','coin_name')
        ]
        unique_together = [
            ('user_id','coin_name','business','business_id')
        ]


