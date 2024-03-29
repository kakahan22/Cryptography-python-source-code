# 实现一个简单的单表代换密码
import math
import string
alph_table1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']

def alphabetic_cipher_table():
    key1 = input('请输入密钥')
    # 根据密钥生成字母表
    # 首先去重,这里需要保持顺序并且去重，可以使用字典，会简洁并且高效
    key2 =list({}.fromkeys(key1).keys())
    key2_len = len(key2)
    print(key2)
    # 我们将abcd啥的和字母表对应起来。


    # 我们先将字母矩阵的顺序生盛出来，然后用切片读取最后的字母表。
    for i in range(26):
        if alph_table1[i] not in key2:
            key2.append(alph_table1[i])
    print('字母矩阵的顺序是', key2)
    # 利用切片再来一个循环
    key_table = ''
    for i in range(key2_len):
        key_table = key_table + ''.join(key2[i::key2_len])
    print('最后字母表为', key_table)
    return key_table

# 进行替换加密
def encrypt(key_table):
    message = input('请输入需要进行简单替换的明文')
    en_text = ''
    for i in range(len(message)):
        en_text = en_text + key_table[ord(message[i]) - ord('a')]

    en_text = ''.join(en_text.split())
    print('密文为', en_text)
    return en_text

# 解密函数为
def decrypt(en_text , key_table):
    # 这里传参就没有重新用最开始密钥来传了，因为其实我们解密也是再算出哪个key_table，不重复
    de_text = ''
    for i in range(len(en_text)):
        de_text = de_text + alph_table1[key_table.index(en_text[i])]
    print('解密后的明文为',de_text)

key_table = alphabetic_cipher_table()
en_text = encrypt(key_table)
decrypt(en_text, key_table)