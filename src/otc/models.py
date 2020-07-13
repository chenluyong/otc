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

    side = models.IntegerField(verbose_name='买单/卖单', help_text='1:卖单/2:买单')
    max_deal_limit = models.FloatField(verbose_name='最大买卖额度')
    min_deal_limit = models.FloatField(verbose_name='最小买卖额度')
    public_info = models.TextField(verbose_name='公告内容')

    card_enable = models.BooleanField(verbose_name='银行卡支持',default=False)
    wechat_enable = models.BooleanField(verbose_name='微信支持',default=False)
    alipay_enable = models.BooleanField(verbose_name='支付宝支持',default=False)

    status = models.IntegerField(verbose_name='订单状态',help_text='0:删除/1:正常/2:撤销',default=False)

    create_at = models.DateTimeField(auto_created=True, verbose_name='创建时间')
    finish_at = models.DateTimeField(auto_now=True,verbose_name='取消时间')

    class Meta:
        ordering = ['create_at']


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    market = models.ForeignKey(Market, related_name='account_otc_market_order', on_delete=models.CASCADE)

    advertiser = models.ForeignKey(User, related_name='account_otc_market_advertiser', on_delete=models.CASCADE,verbose_name='广告主身份')
    side = models.IntegerField(verbose_name='买单/卖单', help_text='1:卖单/2:买单')
    opposite = models.ForeignKey(User, related_name='account_otc_market_advertiser', on_delete=models.CASCADE,verbose_name='客户身份')

    coin_name = models.CharField(max_length=32,verbose_name='币种名称')
    price = models.CharField(max_length=32,verbose_name='价格')
    currency = models.CharField(max_length=32, verbose_name='现金名称',help_text='CNY/USD')
    transact_type = models.CharField(max_length=32, verbose_name='交易方式',help_text='card/wechat/alipay')

    status = models.IntegerField(verbose_name='订单状态',help_text='0:取消/1:等待付款/2:成功',default=2)
    error_status = models.IntegerField(verbose_name='异常状态', help_text='0:无/1:申诉中', default=0)

    create_at = models.DateTimeField(auto_created=True, verbose_name='创建时间')
    finish_at = models.DateTimeField(auto_now=True,verbose_name='完成时间')

    class Meta:
        ordering = ['create_at']


class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='用户')
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name='主订单')
    opposite = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='对手用户')
    side = models.IntegerField(verbose_name='买单/卖单', help_text='1:卖单/2:买单')

    status = models.IntegerField(verbose_name='订单状态',help_text='0:待支付/1:已经支付或放币',default=2)
    error_status = models.IntegerField(verbose_name='异常状态', help_text='0:申诉被拒绝/1:申诉受理/2:申诉已处理/', default=0)

    create_at = models.DateTimeField(auto_created=True, verbose_name='创建时间')
    pay_at = models.DateTimeField(auto_now=True,verbose_name='支付或放币时间')

    class Meta:
        ordering = ['create_at']
