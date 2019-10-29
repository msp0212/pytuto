i = 1
while i <= 10:
    if i == 1:
        print('one')
    elif i == 2:
        print("two")
    elif i == 5:
        i += 1
        continue
    elif i == 7:
        break
    else:
        print(i, end=' ')
    i += 1
