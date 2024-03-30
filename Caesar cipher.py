import random
from math import ceil

# 最大公约数，辗转相除法法，其实math模块里面也有gcd函数
def gcd(a ,b):
    # 原理就是以除数和余数反复做除法运算，当余数为 0 时，取当前算式除数为最大公约数
    if a %b == 0:
         return b
    else:
        return gcd(b, a % b)

# 求逆元,用扩展欧几里得算法，扩展欧几里得算法在求最大公约数的同时还能找到x，y
# 参考解析https://juejin.cn/post/7175914985560752186?from=search-suggest
def exgcd(a, b):
    if b ==0:
        return 1, 0, a
    else:
        x, y, z = exgcd(b, a%b)
        x, y = y, (x-(a//b)*y)
        return x, y, z

def ModReverse(a, p):
    x, y, z = exgcd(a, p)
    if z !=1:
        raise Exception('no solution')
    else:
        return (x + p) % p

# 密钥ab产生函数
def proccesskey():
    # 随机产生就行，这里是为了速度，就没有选择太大的随机数
    while 1:
        a = random.randint(0, 100)
        if gcd(a, 26) == 1:
            break
    b = random.randint(-100,26)
    return a , b

# 加密算法
def encrypto():
    message = input('请输入需要加密的明文')
    # key_a, key_b = proccesskey()
    key_a , key_b = 1, 3
    print(f'产生的密钥a为{key_a},产生的密钥b为{key_b}')
    # 进行加密
    message_len = len(message)
    # 把明文的ascii码转换为对应的字母表中的顺序,字母表从0开始
    message_list = [ord(i)-97 for i in message]
    encrypt_list = []
    encrypt_text = ''
    for i in range(message_len):
        encrypt_list.append((message_list[i] * key_a + key_b) % 26)
        encrypt_text = encrypt_text + chr(encrypt_list[i] + 97)
    print('加密后的密文为', encrypt_text)

    return encrypt_text, key_a, key_b

# 解密函数
def decrypto(encrypt_text, key_a, key_b):
    # 得到逆元
    key_a_reverse = ModReverse(key_a, 26)
    encrypt_list = [ord(i)-97 for i in encrypt_text]
    decrypt_list = []
    decrypt_text = ''
    for i in range(len(encrypt_list)):
        decrypt_list.append(key_a_reverse*(encrypt_list[i] - key_b) % 26)
        decrypt_text = decrypt_text + chr(decrypt_list[i] + 97)
    print('解密后的明文为', decrypt_text)

encrypt_text, key_a, key_b = encrypto()
decrypto(encrypt_text, key_a, key_b)
