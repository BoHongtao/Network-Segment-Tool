# encoding: utf-8
# @author: John
# @contact: BoHongtao@yeah.net
# @software: PyCharm
# @time: 2018/8/27 9:36

# 位数转换成掩码
def intTomask(mask_int):
  bin_arr = ['0' for i in range(32)]
  for i in range(mask_int):
    bin_arr[i] = '1'
  tmpmask = [''.join(bin_arr[i * 8:i * 8 + 8]) for i in range(4)]
  tmpmask = [str(int(tmpstr, 2)) for tmpstr in tmpmask]
  return '.'.join(tmpmask)

# 转换成32位二进制
def ipTransByte(ipParam):
    addrIpTemp = ipParam.split(".")
    tNo0 = bin(int(addrIpTemp[0])).__str__()[2:]
    tNo0 = "0" * (8 - len(tNo0)) + tNo0
    tNo1 = bin(int(addrIpTemp[1])).__str__()[2:]
    tNo1 = "0" * (8 - len(tNo1)) + tNo1
    tNo2 = bin(int(addrIpTemp[2])).__str__()[2:]
    tNo2 = "0" * (8 - len(tNo2)) + tNo2
    tNo3 = bin(int(addrIpTemp[3])).__str__()[2:]
    tNo3 = "0" * (8 - len(tNo3)) + tNo3
    return tNo0 + tNo1 + tNo2 + tNo3

# 函数：掩码转换为数字形式
def MaskToInt(mask):
    i = 0
    ByteMask = ''
    ByteMask = ipTransByte(mask)
    for i in range(0, 32):
        if (ByteMask[i] == "0"):
            return i
    return 32

# 函数：IP地址与地址段进行适配比较(正掩码) in=>0  not in=>1
def ipAdd_Match_Mask(ip1, ip2, mask):
    ipResult = 0
    for i in range(0, 32):
        if (mask[i] == "0"):
            continue
        elif ((mask[i] == "1") and (ip1[i] == ip2[i])):
            continue
        else:
            ipResult = 1
            break
    return ipResult

# 函数：IP地址与地址段进行适配比较(反掩码) in=>0  not in=>1
def ipAdd_Match_WMask(ip1, ip2, wmask):
    ipResult = 0
    for i in range(0, 32):
        if (wmask[i] == "1"):
            continue
        elif ((wmask[i] == "0") and (ip1[i] == ip2[i])):
            continue
        else:
            ipResult = 1
            break
    return ipResult


def is_in_range(ip,ip_seg,mask,flag):
    ip_seg_bin = ipTransByte(ip_seg)
    mask_bin = ipTransByte(mask)
    rs = ipAdd_Match_Mask(ip,ip_seg_bin,mask_bin) if flag == 0 else ipAdd_Match_WMask(ip,ip_seg_bin,mask_bin)
    return True if rs == 0 else False