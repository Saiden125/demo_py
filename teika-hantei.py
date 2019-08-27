teika = input('定価')
if teika.isdigit():
    print(round(int(teika) * 1.08))
    print(round(int(teika) * 1.10))
else:
    print('数字ではない')