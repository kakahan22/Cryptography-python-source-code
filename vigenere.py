# 这里参考了维吉尼亚表格，其实最开始的时候我想的是一个笨蛋方法，就是利用表格找位置
# 后面看了wikipedia对他的加密解法的写法，发现可以用表达式来简化

def processkey(message_len, raw_key):
    key = ''
    key_len = len(raw_key)
    if key_len >= message_len:
        return raw_key
    else:
        for i in range(message_len):
            key = key + raw_key[i % (key_len)]
    print('扩展后的密钥为', key)
    return key

def encrypt():
    message = input('请输入你加密的明文')
    message_len = len(message)
    # 对密钥进行处理,其实这一步密钥的最终确定，一些书直接用关键词代替了，这样只要取模还更方便。
    raw_key = input('请输入你的关键词')
    key = processkey(message_len, raw_key)
    # 加密操作
    encrypt_text = ''
    for i in range(message_len):
        encrypt_text = encrypt_text + chr((ord(message[i])-97 + ord(key[i])-97) % 26 + 97 )
    print('最后的密文为', encrypt_text)
    return encrypt_text , key

# 解密
def decrypt(encrypt_text, key):
    decrypt_text = ''
    for i in range(len(encrypt_text)):
        decrypt_text = decrypt_text + chr(((ord(encrypt_text[i]) - (ord(key[i]) - 97)) - 97) % 26 + 97)
    print('解密后的明文为', decrypt_text)

encrypt_text, key =encrypt()
decrypt(encrypt_text, key)