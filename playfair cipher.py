import math
import copy
def processkey(rawkey):
    # 后面看到把i/j都当作i看，并不是谁先出现选择谁
    if 'j' in rawkey:
        # tips：replace并不是真的替换，而是返回一个副本
        rawkey = rawkey.replace('j', 'i')
    # 去重
    key_list = list({}.fromkeys(rawkey).keys())
    # 创建字母矩阵5*5
    # 这里是先生成字符串后生成矩阵
    key_len = len(key_list)
    for i in range(26):
        if (chr(97 + i) not in key_list) and i != 9:
            key_list.append(chr(97 + i))
        elif (chr(97 + i) not in key_list) and i == 9:
            continue

    key_text = ''.join(key_list)
    print('key_text是', key_text)
    alph_list = []
    counter = 0
    for i in range(5):
        temp_list = []
        for j in range(5):
            temp_list.append(key_list[counter])
            counter = counter + 1
        alph_list.append(temp_list)

    print('最后得到的字母表是', alph_list)
    return alph_list, key_text

# 加密
def encrypt():
    message = input('请输入你需要加密的明文')
    pflag = 0
    # 对明文进行奇偶处理
    if len(message) % 2 == 1:
        message = message + 'z'
        pflag = 1
    rawkey = input('请输入密码关键词')
    alph_list, key_text = processkey(rawkey)

    qflag = 0
    # 对i和j进行处理。
    for i in range(len(message)):
        if message[i] == 'j':
            message = message.replace('j', 'i')
            qflag =1
    #分组，为了展示分组这个步骤，我们还是选择用两个循环来对他们进行分组

    message_list = []
    for i in range(int(len(message)/2)):
        temp_list = []
        for j in range(2):
            temp_list.append(message[i*2+j])
        message_list.append(temp_list)
    print('分组后', message_list)
    # 加密规则
    num1 = 0
    num2 = 1
    # 其实对于位置的判断反而是简单的，就是如何将一个列表的值对应上另一个列表，如果是一维倒还是知道，二维
    # 最开始是想把字母矩阵转化为字符串，1通过算商和余数，得到第几行，第几列进行比较
    # 暂时只想到这样，如果大家有更好的办法，再改吧。
    en_text =''
    # 这样就不用循环生成一个了。
    en_list = copy.deepcopy(message_list)
    for i in range(int(len(message)/2)):
        x = message_list[i][0]
        y = message_list[i][1]
        line_x = key_text.index(x)//5
        column_x = key_text.index(x) % 5
        line_y = key_text.index(y)//5
        column_y = key_text.index(y) % 5
        if line_x == line_y:
            en_list[i][0] = alph_list[line_x][(column_x+1) % 5]
            en_list[i][1] = alph_list[line_y][(column_y+1) % 5]
            en_text = en_text + en_list[i][0]
            en_text = en_text + en_list[i][1]
        elif column_x == column_y:
            en_list[i][0] = alph_list[(line_x + 1) % 5][column_x]
            en_list[i][1] = alph_list[(line_y + 1) % 5][column_y]
            en_text = en_text + en_list[i][0]
            en_text = en_text + en_list[i][1]
        else:
            # 其实找到对角线这个我非常不知道,因为开始是根据大小来的，后来发现这样解密的时候就根本不知道顺序了后来
            # 注意到书上写了一个同行原则，所以我们这样的话就知道该如何进行破解了。
            temp_alphx = alph_list[line_x][column_y]
            temp_alphy = alph_list[line_y][column_x]
            en_list[i][0] = temp_alphx
            en_list[i][1] = temp_alphy
            en_text = en_text + en_list[i][0]
            en_text = en_text + en_list[i][1]
    # 得到了加密后的结果
    print('加密后的矩阵为', en_list)
    # 密文
    print('密文为', en_text)
    return en_text, rawkey, en_list, alph_list, key_text ,pflag, qflag


# 解密, 这里传送参数，为了不多写一次程序，直接把分组后的结果也传输过去了，免得麻烦，如果你需要的话，就自己修改一下，把encrypt的处理复制粘贴上去。
def decrypt(en_text, rawkey, en_list, alph_list, key_text, pflag, qflag):
    # 因为直接传过来了都分好组的结果，我们直接用变换规则就可以了
    de_text = ''
    de_list = copy.deepcopy(en_list)
    for i in range(len(en_text)//2):
        x = en_list[i][0]
        y = en_list[i][1]
        line_x = key_text.index(x) // 5
        column_x = key_text.index(x) % 5
        line_y = key_text.index(y) // 5
        column_y = key_text.index(y) % 5
        if line_x == line_y:
            de_list[i][0] = alph_list[line_x][(column_x - 1) % 5]
            de_list[i][1] = alph_list[line_y][(column_y - 1) % 5]
            de_text = de_text + de_list[i][0]
            de_text = de_text + de_list[i][1]
        elif column_x == column_y:
            de_list[i][0] = alph_list[(line_x - 1) % 5][column_x]
            de_list[i][1] = alph_list[(line_y - 1) % 5][column_y]
            de_text = de_text + de_list[i][0]
            de_text = de_text + de_list[i][1]
        else:
            temp_alphx = alph_list[line_x][column_y]
            temp_alphy = alph_list[line_y][column_x]
            de_list[i][0] = temp_alphx
            de_list[i][1] = temp_alphy
            de_text = de_text + de_list[i][0]
            de_text = de_text + de_list[i][1]

    # 解密后的结果
    print('解密矩阵为', de_list)
    if pflag == 1:
        de_text = de_text[:-1]# 删除要用切片，不能用减法，真的想不通自己用减法实在想什么

    if qflag == 1:
        de_text = de_text.replace('i', 'j')
    print('解密后的明文为', de_text)


en_text, rawkey, en_list, alph_list, key_text, pflag, qflag= encrypt()
decrypt(en_text, rawkey, en_list, alph_list, key_text, pflag, qflag)
# 在看到那个表的时候，我发现另外的书上生成表的顺序是打乱的，所以这个表的选取其实也没有很特定的规则。