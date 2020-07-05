from django.contrib import admin

# Register your models here.
from atm.models import History, Deposit



# class History(models.Model):
#     id = models.AutoField(primary_key=True)
#
#     blockchain = models.CharField(max_length=32, verbose_name='区块网络')
#     coin_name = models.CharField(max_length=32, verbose_name='币种名称')
#     txid = models.CharField(max_length=128, verbose_name='交易编号',unique=True)
#     address = models.CharField(max_length=128, verbose_name='地址')
#     address_tag = models.CharField(max_length=64, verbose_name='地址标签', null=True)
#
#     type = models.IntegerField(verbose_name='交易类型', help_text='1：充值，10：扣款')
#     order_amount = models.FloatField(verbose_name='订单金额',default=0)
#     fee = models.FloatField(verbose_name='手续费',default=0)
#     discount_amount = models.FloatField(verbose_name='优惠金额', default=0)
#     discount_reason = models.CharField(max_length=128, verbose_name='优惠说明', null=True)
#     actual_amount = models.FloatField(verbose_name='实际金额', help_text = 'actual_amount = order_amount - fee + discount_amount')
#
#     status = models.CharField(max_length=32, verbose_name='状态', choices=STATUS_TYPE)
#     error_code = models.CharField(max_length=32, verbose_name='错误代码', null=True)
#     error_message = models.CharField(max_length=256, verbose_name='错误内容', null=True)
#
#     user = models.ForeignKey(AccountInfoModel, on_delete=models.CASCADE, null=True)
#     balance = models.ForeignKey(BalanceHistoryModel,on_delete=models.CASCADE, null=True)
#     refund_id = models.IntegerField(verbose_name='退款编号', null=True)
#
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('txid','blockchain','coin_name','address','address_tag','type','user','discount_reason','created_at')
    # fields = (('blockchain','coin_name'),'address')
    search_fields = ('coin_name',)
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 25
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('-created_at',)

    # list_editable 设置默认可编辑字段
    list_editable = ['discount_reason']
    # 对日期进行分类
    date_hierarchy = 'created_at'

    # 字段为空时的默认显示
    empty_value_display = '-'



admin.site.register(History,HistoryAdmin)