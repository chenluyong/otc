from django.db import models

# Create your models here.

from account.models import Info as User

TRANSACT_TYPE = (
    ('TRANSFER', 'transfer'),  # 划转
    ('DEPOSIT', 'deposit'),  # 充值
    ('WITHDRAW', 'withdraw'),  # 提现
    ('WITHDRAW_FEE', 'withdraw_fee'),  # 提现手续费
    ('REBATE', 'rebate'),  # 交易返佣
    ('DEDUCTION', 'deduction'),  # 手续费抵扣
    ('OTHER', 'other'),  # 其它
)


# 总财务账单
class History(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, related_name='account_balance_history', on_delete=models.CASCADE)
    username = models.CharField(max_length=128,verbose_name='-账号')
    coin_name = models.CharField(max_length=32, verbose_name='币种名称')
    business = models.CharField(max_length=32, verbose_name='引发变更的业务',help_text='transfer/deposit/withdraw')
    change = models.FloatField(verbose_name='变更金额')
    balance = models.FloatField(verbose_name='余额')
    prev_id = models.IntegerField(verbose_name='上一笔账单编号',unique=True,null=True)
    change_at = models.DateTimeField(auto_now_add=True, verbose_name='变更时间')
    detail = models.TextField(verbose_name='更多信息',help_text='充值提现ID等')
    order_id = models.IntegerField(verbose_name='订单详情编号',help_text='根据business来决定订单所属的表')

    class Meta:
        ordering = ['change_at']


