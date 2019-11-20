
def make_banner(text):
    # Write code here
    # 将所有字符改为小写
    text = text.lower()
    try:
        # 测试接受的参数中是存在非字母字符
        for t in text:
            if not 'a' <= t <= 'z':
                # 引发错误
                raise ValueError("ValueError: All characters in text must be alphabetic.")
    # 捕获异常
    except ValueError as e:
        print(e)
        return ''

    letters = []
    # 读取banner_letters.txt文件中内容
    with open('banner_letters.txt', 'r') as f:
        for line in f.readlines():
            # 去除每行的换行符并加入列表中
            letters.append(line.strip('\n'))
    print(len(letters))
    # 用于保存要返回各行字符列表
    results = []
    # 通过获取所有字符的ascii码并减去97来获取字符在数据中的索引
    indexes = []
    for t in text:
        indexes.append(ord(t) - 97)
    # 分行获取多个字符的第0－7行符号
    for i in range(7):
        line = []
        # 遍历字符序号，并获取各字符对应行的数据
        for index in indexes:
            line.append(letters[index * 7 + i])
        # 各字符符号数据之间添加空格
        line = ' '.join(line)
        results.append(line)
    # 各行字符数据之间添加换行符
    results = '\n'.join(results)
    return results

print(make_banner('ebks'))
    
