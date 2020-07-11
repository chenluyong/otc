from django.db import models

# Create your models here.



class Coin(models.Model):
    coin_name = models.CharField(max_length=32, verbose_name='币种名称')
    blockchain = models.CharField(max_length=32, verbose_name='公链网络')

# 总财务账单
class History(models.Model):
    id = models.AutoField(primary_key=True)

    user_id = models.IntegerField(verbose_name='用户编号')
    coin_name = models.CharField(max_length=32, verbose_name='币种名称')
    business = models.CharField(max_length=32, verbose_name='引发变更的业务',help_text='transfer/deposit/withdraw')
    business_id = models.IntegerField(verbose_name='订单详情编号',help_text='根据business来决定订单所属的表')
    change = models.FloatField(verbose_name='变更金额')
    balance = models.FloatField(verbose_name='活跃余额')
    freeze_balance = models.FloatField(verbose_name='冻结余额',default=0)
    prev_id = models.IntegerField(verbose_name='上一笔账单编号',unique=True,null=True)
    change_at = models.FloatField(verbose_name='变更时间')
    detail = models.TextField(verbose_name='更多信息{object}',help_text='更多信息',null=True)


    def update_balance(self):
        balances = History.objects.filter(user_id=self.user_id, coin_name=self.coin_name)[:1]

        prev_id = None
        if len(balances) != 0:
            balance = balances[0]
            prev_id = balance.id
            self.prev_id = prev_id

            self.balance = balance.balance + self.change

            if self.balance < 0 :
                raise Exception("balance not enough!")

            import time
            self.change_at = time.time()

            self.save()


    class Meta:
        ordering = ['-change_at']
        index_together = [
            ('user_id','coin_name')
        ]


