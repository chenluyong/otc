from django.db import models

# Create your models here.

from django.db import models

class Ticker(models.Model):
    name = models.CharField(max_length=32)
    symbol = models.CharField(max_length=32)

    base = models.CharField(max_length=32)
    currency = models.CharField(max_length=32)

    high = models.CharField(max_length=64)
    low = models.CharField(max_length=64)
    close = models.CharField(max_length=64)
    source = models.CharField(max_length=128)

    created = models.DateTimeField(auto_now_add=True)
    # title = models.CharField(max_length=100, blank=True, default='')
    # code = models.TextField()
    # linenos = models.BooleanField(default=False)
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    #
    # owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    # highlighted = models.TextField()
    #
    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = 'table' if self.linenos else False
    #     options = {'title': self.title} if self.title else {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                               full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super(Snippet, self).save(*args, **kwargs)


    class Meta:
        ordering = ['created']