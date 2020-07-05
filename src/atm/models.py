from django.db import models

# Create your models here.
from balance.models import History as BalanceHistoryModel
from account.models import Info as AccountInfoModel

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

class History(models.Model):
    id = models.AutoField(primary_key=True)

    blockchain = models.CharField(max_length=32, verbose_name='区块网络')
    coin_name = models.CharField(max_length=32, verbose_name='币种名称')
    txid = models.CharField(max_length=128, verbose_name='交易编号',unique=True)
    address = models.CharField(max_length=128, verbose_name='地址')
    address_tag = models.CharField(max_length=64, verbose_name='地址标签', null=True)

    type = models.IntegerField(verbose_name='交易类型', help_text='1：充值，0：扣款')
    order_amount = models.FloatField(verbose_name='订单金额',default=0)
    fee = models.FloatField(verbose_name='手续费',default=0)
    discount_amount = models.FloatField(verbose_name='优惠金额', default=0)
    discount_reason = models.CharField(max_length=128, verbose_name='优惠说明', null=True)
    actual_amount = models.FloatField(verbose_name='实际金额', help_text = 'actual_amount = order_amount - fee + discount_amount')

    status = models.CharField(max_length=32, verbose_name='状态', choices=STATUS_TYPE)
    error_code = models.CharField(max_length=32, verbose_name='错误代码', null=True)
    error_message = models.CharField(max_length=256, verbose_name='错误内容', null=True)

    user = models.ForeignKey(AccountInfoModel, on_delete=models.CASCADE, null=True)
    balance = models.ForeignKey(BalanceHistoryModel,on_delete=models.CASCADE, null=True)
    refund_id = models.IntegerField(verbose_name='退款编号', null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')


class Deposit(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(AccountInfoModel,on_delete=models.CASCADE, null=True)

    blockchain = models.CharField(max_length=32, verbose_name='区块网络')
    coin_name = models.CharField(max_length=32, verbose_name='币种名称')
    address = models.CharField(max_length=128, verbose_name='地址',unique=True)
    prev_address = models.CharField(max_length=128, verbose_name='被弃用的地址',unique=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_use_at = models.DateTimeField(auto_now_add=True, verbose_name='被使用时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')