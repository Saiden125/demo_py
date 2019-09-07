text = input('年齢入力')
if text.isdigit():
    age = int(text)
    if age < 20:
        print('未成年')