
import struct, sys, os, time
from platform import python_version

from ip.utils.ip2Region import Ip2Region

dbFile = './ip/utils/ip2region.db'
# dbFile = 'F:/projects/2020/we/ip2region/data/ip.merge.txt'
searcher = Ip2Region(dbFile)
def search(_ip):
    # line = "112.12.242.40"

    if not searcher.isip(_ip):
        print("[Error]: Invalid ip address.")

    data = searcher.memorySearch(_ip)

    ret = "未知地址"
    try:
        ret = data["region"].decode('utf-8')
    except Exception as e:
        print("[Error]: %s" % e)

    # searcher.close()

    return ret
