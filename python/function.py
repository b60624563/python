def sysout(msg, count):
    'test'

    for i in range(0, count): 
        print(str(i) + '_' + msg)

    return count**2


res = sysout('a', 5)

print(res)

# 類似 null 的存在
a = None

