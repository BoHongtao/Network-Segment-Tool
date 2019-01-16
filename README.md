# base-ip
之前在做一些ip计算，在判断掩码的时候，比如判断一个ip是否在127.0.0.1/24中
费劲千辛万苦，发现了一个简单的方法

1,ip->32位二进制，ip1,ip2 --> ip_bin1,ip_bin2;<br/>
2,掩码->32数字;<br/>
3, 根据是正掩码或者反掩码调用不同的方法;<br/>
# 对于两个网段的比较，可以使用IPy这个库，不需要自己造轮子
from IPy import IP<br/>
IP('192.168.1.0/24') in IP('192.168.0.0/32')<br/>
# 区分内外网函数
这里传递的是网段，然后从网段中取出任意一个ip来判断
    from IPy import IP
    def is_trust(ip_mask):
    ips = IP(ip_mask)
    for tmp in ips:
    ip = str(tmp)
    break
    if(ip.startswith('10')):
    return True
    elif ip.startswith('172'):
    if(ip.startsWith('172.1') & ip[5]>'6' & ip[6] == '.'):
    return True
    elif(ip.startswith('172.2') & ip[6] == '.'):
    return True
    elif(ip.startswith("172.3") & ip[5] <= '1'):
    return True
    else:
    return False
    elif(ip.startswith("192.168")):
    return True
    else:
    return False
    print(is_trust('222.175.113.226/32'))

