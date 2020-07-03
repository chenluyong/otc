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
class Info(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, related_name='account_bill', on_delete=models.CASCADE)
    username = models.CharField(max_length=128,verbose_name='账号')
    billing_cycle = models.CharField(max_length=32,verbose_name='账期',help_text='YYYY-MM,按月查账单')
    currency = models.CharField(max_length=32, verbose_name='币种名称')

    type = models.IntegerField(verbose_name='交易类型', help_text='1：充值，10：扣款')
    transact_type = models.CharField(max_length=32, choices=TRANSACT_TYPE, verbose_name='订单类型')
    payable_payment_amount = models.FloatField(verbose_name='应当付款金额')
    fee = models.FloatField(verbose_name='手续费')
    discount_amount = models.FloatField(verbose_name='优惠金额',default=0)
    discount_reason = models.CharField(verbose_name='优惠说明')
    actual_payment_amount = models.FloatField(verbose_name='实际付款金额',help_text='实付=应付+手续费-优惠金额')
    available_balance = models.FloatField(verbose_name='可用余额')
    freeze_balance = models.FloatField(verbose_name='可用余额')
    account_balance = models.FloatField(verbose_name='账户总余额')

    prev_id = models.IntegerField(verbose_name='上一笔账单编号')

    transact_at = models.DateTimeField(auto_now_add=True, verbose_name='交易时间')

