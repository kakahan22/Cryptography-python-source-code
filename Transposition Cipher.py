# 处理获得密钥的长度和顺序。
def processsecrektkey(s):
    sLength = len(s)
    tmplist = []
    for i in range(len(s)):
        char = s[i]
        # 把templist存入字母的ascii码值
        tmplist.append(ord(char))
    sKey = list()
    sort_tmplist = sorted(tmplist)
    for index, value in enumerate(tmplist):
        sKey.append(sort_tmplist.index(value)+1)
    print('tmplist:', tmplist)
    print('sKey', sKey)
    return sKey , sLength

def encrypt():
    print('-' * 20)
    # 获取明文
    text = input('请输入明文：')
    # 去除空格
    text = text.split(" ")
    text = "".join(text)
    # 明文长度
    text_len = len(text)
    print('明文为%s,明文长度为%d'%(text, text_len))
    # 获取密钥
    key = input('请输入密钥:')
    # 获取密钥长度和密钥对应的顺序
    sKey , key_len = processsecrektkey(key)
    print("密钥长度为", key_len)
    print("密钥数学顺序为", sKey)
    # 来判断是否需要补充空格
    while text_len % key_len != 0:
        text = text + " "
        text_len = text_len +1
    print(f"在周期已定的情况下，补充空格后的明文为{text}, 明文长度为{text_len}")
    # 利用一个二维list对明文根据周期进行分割
    tmpgroup = list()
    group = list()
    counter = 1
    for item in text:
        if counter % key_len != 0:
            tmpgroup.append(item)
            counter = counter + 1
        else:
            tmpgroup.append(item)
            group.append(tmpgroup)
            tmpgroup = []
            counter = counter + 1

    print('分组后的明文为')
    for i in group:
        for item in i:
            print(item , end=' ')
        print()
    # 对明文进行加密
    crypt_text = []
    tmp_crypt_text = []
    counter_cry = 0
    for i in group:
        tmp_crypt_text = [''] * key_len
        for index, value in enumerate(i):
           tmp_crypt_text[sKey[index] - 1] = i[index]
        crypt_text.append(tmp_crypt_text)
    # 加密后的结果
    cry_text = ""
    print('加密后的分组密文为')
    for i in crypt_text:
        for item in i:
            cry_text = cry_text + item
            print(item, end=' ')
        print()
    print(f"最后的密文为{cry_text}")
    return text, cry_text , sKey

# 解密
def decrypt(cry_text, sKey):
    print('-' * 20)
    # 对密文进行分割
    tmpgroup = list()
    group = list()
    counter = 1
    for item in cry_text:
        if counter % len(sKey) != 0:
            tmpgroup.append(item)
            counter = counter + 1
        else:
            tmpgroup.append(item)
            group.append(tmpgroup)
            tmpgroup = []
            counter = counter + 1

    print('分组后的密文为')
    for i in group:
        for item in i:
            print(item, end=' ')
        print()
    # 解密，求逆置换
    re_sKey=[""] * len(sKey)
    for index , value in enumerate(sKey):
        re_sKey[value-1] = index + 1

    # 进行解密
    decode_text = []
    tmp_decode_text = []
    counter_dec = 0
    for i in group:
        tmp_decode_text = [''] * len(re_sKey)
        for index, value in enumerate(i):
            tmp_decode_text[re_sKey[index] - 1] = i[index]
        decode_text.append(tmp_decode_text)
    dec_text = ""
    print('解密后的分组明文为')
    for i in decode_text:
        for item in i:
            dec_text = dec_text + item
            print(item, end=' ')
        print()
    print(f"最后的解密明文为{dec_text}")

if __name__ =='__main__':
    text, cry_text , sKey = encrypt()
    decrypt(cry_text , sKey)