# Generated by Django 3.0.7 on 2020-06-30 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='buy_trade_count',
            field=models.IntegerField(default=0, verbose_name='买单订单总数量'),
        ),
        migrations.AddField(
            model_name='info',
            name='cancel_time_avg',
            field=models.CharField(default='0', max_length=32, verbose_name='平均取消订单速度'),
        ),
        migrations.AddField(
            model_name='info',
            name='margin_amount',
            field=models.IntegerField(default=0, verbose_name='保证金'),
        ),
        migrations.AddField(
            model_name='info',
            name='month_trade_count',
            field=models.IntegerField(default=0, verbose_name='月订单成交数量'),
        ),
        migrations.AddField(
            model_name='info',
            name='order_complete_rate',
            field=models.IntegerField(default=0, verbose_name='成交订单概率'),
        ),
        migrations.AddField(
            model_name='info',
            name='release_time_avg',
            field=models.CharField(default='0', max_length=32, verbose_name='平均放币时长'),
        ),
        migrations.AddField(
            model_name='info',
            name='sell_trade_count',
            field=models.IntegerField(default=0, verbose_name='卖单订单总数量'),
        ),
        migrations.AddField(
            model_name='info',
            name='trade_count',
            field=models.IntegerField(default=0, verbose_name='总订单成交数量'),
        ),
    ]