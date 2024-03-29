# 这里对二维列表整个列进行操作的方法，借鉴了文章https://blog.51cto.com/u_16213337/8812842

import math
# 对密钥转化为对应的key的顺序
def processsecretkey(s):
    s_len = len(s)
    tempslist = []
    for i in range(len(s)):
        tempslist.append(ord(s[i]))
    skey = []
    sorted_tempslist = sorted(tempslist)
    for index , value in enumerate(sorted_tempslist):
        skey.append(tempslist.index(value) + 1)

    print('skey:', skey)
    return skey, s_len

# 加密
def encrypt():
    message = input("请输入需要进行加密的明文")
    s_key = input("请输入密钥")
    # 对密钥进行处理
    skey, s_len = processsecretkey(s_key)
    # 对明文进行列矩阵的排列，后面用空填补不满
    message_len = len(message)
    line_number = math.ceil(message_len / s_len)
    # 明文矩阵
    message_matrix = []
    temp_matrix = []
    counter = 0
    for i in range(line_number):
        temp_matrix = []
        for j in range(s_len):
            if counter < message_len:
                temp_matrix.append(message[counter])
                counter = counter +1
            else:
                temp_matrix.append(' ')
        message_matrix.append(temp_matrix)
    # print(message_matrix)
    # 进行加密计算
    encrypt_text = ''
    for i in skey:
        for j in range(line_number):
            encrypt_text = encrypt_text + message_matrix[j][i-1]

    encrypt_text = ''.join(encrypt_text.split())
    print('加密后的密文为：', encrypt_text)
    return encrypt_text , skey

# 解密函数
def decrypt(encrypt_text , skey):
    # 创建密文矩阵
    entext_len = len(encrypt_text)
    s_len = len(skey)
    line_number = math.ceil(entext_len/s_len)
    en_matrix = []
    temp_matrix = []
    counter = 0
    # 在这个求矩阵分组的时候我们需要注意，我们目前得到的密文，分组之后其实是原来的转了90度，大家理解一下。
    for i in range(s_len):
        temp_matrix = []
        for j in range(line_number):
            if counter < entext_len:
                temp_matrix.append(encrypt_text[counter])
                counter = counter + 1
            else:
                temp_matrix.append(' ')
        en_matrix.append(temp_matrix)
    print(en_matrix)
    # 求逆密钥
    de_key = [''] * s_len
    for index, value in enumerate(skey):
        de_key[value -1 ] = index +1
    print(de_key)
    print(de_key)
    # 解密运算,我们因为反转了90度所以直接对列进行读取就能得到明文
    decrypt_text = ''
    for i in range(line_number):
        for j in range(s_len):
            decrypt_text = decrypt_text + en_matrix[j][i]
    decrypt_text = ''.join(decrypt_text.split())
    print('解密后的明文为',decrypt_text)


encrypt_text , skey = encrypt()
decrypt(encrypt_text , skey)
