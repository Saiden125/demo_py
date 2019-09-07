text = input('年齢入力')
if text.isdigit():
    age = int(text)
    if age < 20:
        if 0 <= age < 6:
            print('未成年(幼児)')
        elif age >= 6 and age <= 15:
            print('未成年(義務教育期間)')
        else:
            print('未成年')
    elif age < 65:
        print('成人')
    else:
        print('高齢者')