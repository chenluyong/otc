class AppSettings(object):

    def __init__(self, prefix):
        self.prefix = prefix

    def _setting(self, name, dflt):
        from django.conf import settings
        getter = getattr(settings,
                         'BALANCE_SETTING_GETTER',
                         lambda name, dflt: getattr(settings, name, dflt))
        return getter(self.prefix + name, dflt)

    @property
    def ACCOUNT_CHECK_ENDPOINT(self):
        return self._setting('ACCOUNT_CHECK_ENDPOINT', {
            'default':'http://192.168.1.61:8080/account/check/',
        })


    @property
    def SUPPORT_ASSETS(self):
        return self._setting('ASSETS', ['BTC','USDT'])



# Ugly? Guido recommends this himself ...
# http://mail.python.org/pipermail/python-ideas/2012-May/014969.html
import sys  # noqa


app_settings = AppSettings('BALANCE_')
app_settings.__name__ = __name__
sys.modules[__name__] = app_settings
#