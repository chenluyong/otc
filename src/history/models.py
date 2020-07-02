from django.db import models


# Create your models here.
from account.models import Info as User

TRANSACT_TYPE=(
    ('TRANSFER','transfer'), # 划转
    ('DEPOSIT','deposit'), # 充值
    ('WITHDRAW', 'withdraw'), # 提现
    ('WITHDRAW_FEE', 'withdraw_fee'), # 提现手续费
    ('REBATE', 'rebate'), # 交易返佣
    ('DEDUCTION','deduction'), # 手续费抵扣
    ('OTHER', 'other'), # 其它
)

# 总财务账单
class Info(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, related_name='account_history', on_delete=models.CASCADE)
    coin_name = models.CharField(max_length=32, verbose_name='币种名称')

    type = models.IntegerField(verbose_name='交易类型', help_text='1：充值，10：提现')
    transact_type = models.CharField(max_length=32, choices=TRANSACT_TYPE, verbose_name='订单类型')
    amount = models.CharField(max_length=64,verbose_name='交易金额')
    fee = models.CharField(max_length=64,verbose_name='手续费')
    available_balance = models.CharField(max_length=64, verbose_name='可用余额')
    account_balance = models.CharField(max_length=64, verbose_name='账户总余额')

    prev_history_id = models.IntegerField(verbose_name='上一笔账单编号')

    transact_at = models.DateTimeField(auto_now_add=True, verbose_name='交易时间')


STATUS_TYPE = (
    # Withdraw
    ('VERIFY','verifying'), # 待验证
    ('FAILED', 'failed'), # 验证失败
    ('SUBMIT', 'submitted'), # 已提交
    ('REEXAMINE','reexamine'), # 审核中
    ('CANCEL','canceled'), # 已撤销
    ('PASS','pass'), # 审核通过
    ('REJECT','reject'), # 审核拒绝
    ('PRE_TRANSFER', 'pre_transfer'), # 处理中
    ('WALLET_TRANSFER','wallet_transfer'), # 已汇出
    ('WALLET_REJECT', 'wallet_reject'), # 钱包拒绝
    ('CONFIRM_ERROR','confirm_error'), # 区块确认错误
    ('REPEAL','repealed'), # 交易被废止

    ('CONFIRM','confirmed'), # 区块已确认

    # Deposit
    ('UNKNOWN','unknown'), # 未知
    ('CONFIRMING','confirming'), # 确认中
    ('SAFE','safe'), # 不可逆区块
    ('ORPHAN','orphan'), # 待确认
)

# 充提币订单
class DepositWithdraw(models.Model):

    type = models.IntegerField(verbose_name='交易类型', help_text='1：充值，10：提现')

    txid = models.CharField(max_length=128, verbose_name='交易编号')
    blockchain = models.CharField(max_length=32, verbose_name='区块网络')
    coin_name = models.CharField(max_length=32, verbose_name='币种名称')

    amount = models.FloatField(verbose_name='金额')
    fee = models.FloatField(verbose_name='手续费')

    address = models.CharField(max_length=128, verbose_name='地址')
    address_tag = models.CharField(max_length=64, verbose_name='地址标签')


    status = models.CharField(max_length=32, verbose_name='状态',choices=STATUS_TYPE)
    error_code = models.CharField(max_length=32, verbose_name='错误代码')
    error_message = models.CharField(max_length=256, verbose_name='错误内容')

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='最后更新时间')





