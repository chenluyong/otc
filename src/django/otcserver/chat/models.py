from django.db import models

# Create your models here.
from account.models import Info as User

# 命令
class Command(models.Model):
    id = models.AutoField(primary_key=True)
    cmd = models.CharField(max_length=64, verbose_name='命令')
    reply = models.TextField(verbose_name='回复内容')


# 聊天记录
class Record(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account_history', on_delete=models.CASCADE)

    chat_id = models.IntegerField(verbose_name='telegram聊天编号')

    talker_id = models.CharField(max_length=32,verbose_name='谈话者身份编号')
    talker_name = models.CharField(max_length=64, verbose_name='谈话者名称')

    content = models.TextField(verbose_name='聊天内容')
    reply = models.TextField(verbose_name='回复内容')

    chat_at = models.DateTimeField(verbose_name='聊天发起时间')
    reply_at = models.DateTimeField(verbose_name='回复时间')


