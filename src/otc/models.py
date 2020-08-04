from django.db import models
# Create your models here.


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(verbose_name='用户编号',unique=True)

    # OTC 账户
    trade_count = models.IntegerField(verbose_name='总订单成交数量',default=0)
    month_trade_count  = models.IntegerField(verbose_name='月订单成交数量',default=0)
    buy_trade_count  = models.IntegerField(verbose_name='买单订单总数量',default=0)
    sell_trade_count = models.IntegerField(verbose_name='卖单订单总数量',default=0)

    order_complete_rate = models.IntegerField(verbose_name='成交订单概率',default=0)
    release_time_avg = models.CharField(max_length=32,verbose_name='平均放币时长',default='0')
    cancel_time_avg = models.CharField(max_length=32, verbose_name='平均取消订单时长',default='0')

    margin_amount = models.IntegerField(verbose_name='保证金',default=0,help_text='冻结资金，算在用户总资产中')


class CoinList(models.Model):
    id = models.AutoField(primary_key=True)
    coin_name = models.CharField(max_length=32,verbose_name='币种名称')
    limit_amount = models.FloatField(verbose_name='最低发布数量')
    status = models.BooleanField(verbose_name='是否启用')

class Market(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, related_name='account_otc_market', on_delete=models.CASCADE)

    coin =  models.ForeignKey(CoinList, related_name='coin', on_delete=models.CASCADE)
    coin_name = models.CharField(max_length=32,verbose_name='币种名称')
    price = models.CharField(max_length=32,verbose_name='价格')
    currency = models.CharField(max_length=32, verbose_name='现金名称',help_text='CNY/USD')

    side = models.IntegerField(verbose_name='广告类型', help_text='1:卖单/2:买单')
    max_deal_limit = models.FloatField(verbose_name='最大买卖额度')
    min_deal_limit = models.FloatField(verbose_name='最小买卖额度')
    public_info = models.TextField(verbose_name='公告内容')

    bank_name = models.CharField(verbose_name='银行名字')

    status = models.IntegerField(verbose_name='订单状态',help_text='0:删除/1:正常/2:撤销',default=False)

    create_at = models.DateTimeField(auto_created=True, verbose_name='创建时间')
    finish_at = models.DateTimeField(auto_now=True,verbose_name='取消时间')

    class Meta:
        ordering = ['create_at']


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    market = models.ForeignKey(Market,verbose_name='广告编号', related_name='account_otc_market_order', on_delete=models.CASCADE)

    user_id = models.IntegerField(verbose_name='用户编号')
    opposite_id = models.IntegerField(verbose_name='对手编号')

    side = models.IntegerField(verbose_name='买单/卖单', help_text='1:卖单/2:买单')

    coin_name = models.CharField(max_length=32,verbose_name='币种名称')
    price = models.CharField(max_length=32,verbose_name='价格')
    currency = models.CharField(max_length=32, verbose_name='现金名称',help_text='CNY/USD')
    transact_type = models.CharField(max_length=32, verbose_name='交易方式',help_text='card/wechat/alipay')

    status = models.IntegerField(verbose_name='订单状态',help_text='0:成功/1:取消/2:等待付款/3:等待放币/4:申诉中/5:申诉完结',default=2)


    created_at = models.DateTimeField(auto_created=True, verbose_name='创建时间')
    user_payed_at = models.DateTimeField(auto_now=True,verbose_name='用户支付时间')
    opposite_payed_at = models.DateTimeField(auto_now=True, verbose_name='对手支付时间')
    finished_at = models.DateTimeField(auto_now=True,verbose_name='完成时间')

    sues_status = models.IntegerField(verbose_name='异常状态', help_text='0:无/1:提交申诉/2:申诉已受理/3:申诉已处理/4:申诉被拒绝', default=0)
    sues_submitted_at = models.DateTimeField(auto_now=True,verbose_name='提交申诉时间')
    sues_accepted_at = models.DateTimeField(auto_now=True, verbose_name='受理申诉时间')
    sues_processed_at = models.DateTimeField(auto_now=True, verbose_name='处理申诉时间')
    sues_finished_at = models.DateTimeField(auto_now=True, verbose_name='完结申诉时间')

    class Meta:
        ordering = ['create_at']
