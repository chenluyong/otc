



class Ticker:

    host = "47.96.171.142"
    user = 'root'
    pswd = '123456'
    dbname = 'echain'


    def __init__(self, _exchange_name):
        self.exchange_name = _exchange_name

    def set_database(self, _host, _user, _pswd, _dbname):
        self.host = _host
        self.user = _user
        self.pswd = _pswd
        self.dbname = _dbname

    def update(self,_coin, _currency, _symbol, _high, _low, _open, _close, _exchange_name, _time):
        pass
