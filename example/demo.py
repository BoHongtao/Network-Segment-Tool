# encoding: utf-8
# @author: John
# @contact: BoHongtao@yeah.net
# @software: PyCharm
# @time: 2018/8/27 10:17

from baseip.baseip import ipTransByte
from baseip.baseip import intTomask
from baseip.baseip import is_in_range

ip1 = "127.0.0.1"
mask = intTomask(24)
ip2 = "127.0.0.1"

ip1_bin = ipTransByte(ip1)
rs = is_in_range(ip1_bin,ip2,mask,0)

print(rs)
