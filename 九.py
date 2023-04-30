def nine(s):
    tmp = ''
    for x in s:
        tmp += str(int.from_bytes(x.encode('UTF-8'), byteorder='big'))
    return tmp

def Nine(s):
    tmp = s
    for x in range(9):
        tmp = nine(tmp)
    print(int(tmp))

Nine("ddddd")