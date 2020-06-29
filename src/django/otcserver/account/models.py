from django.db import models

from django.contrib.auth.models import AbstractUser




class Info(AbstractUser):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(verbose_name='昵称', null=True, max_length=32)
    is_email_confirmed = models.BooleanField(default=False)
    bio = models.TextField(null=True,)
    avatar_url = models.FileField(upload_to='avatar/', default="/avatar/default_avatar.jpg")
    phone = models.CharField(max_length=11, null=True, unique=True)



    # owner = models.ForeignKey('auth.User', related_name='account', on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_now_add=True)
    # recently_trade_count = models.IntegerField(default=0)
    # last_trade_time = models.DateTimeField(auto_now=True)
    # title = models.CharField(max_length=100, blank=True, default='')
    # code = models.TextField()
    # linenos = models.BooleanField(default=False)
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)


    # highlighted = models.TextField()

    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
        # lexer = get_lexer_by_name(self.language)
        # linenos = 'table' if self.linenos else False
        # options = {'title': self.title} if self.title else {}
        # formatter = HtmlFormatter(style=self.style, linenos=linenos,
        #                           full=True, **options)
        # self.highlighted = highlight(self.code, lexer, formatter)
        # super(OtcAccount, self).save(*args, **kwargs)


    # class Meta:
        # ordering = ['joined_at']


class InfoProviders(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Info, related_name='account', on_delete=models.CASCADE)
    provider = models.CharField(max_length=100,verbose_name='第三方机构名称')
    identifier = models.CharField(max_length=100,verbose_name='第三方机构标识')
    create_at = models.DateTimeField(auto_now_add=True)
    last_login_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'account_info_providers'
        unique_together = (
            ('provider','identifier')
        )