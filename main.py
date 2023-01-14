Alf = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
       'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
while True:
    oper = int(input('Введите число "0" - шифрование,"1" - дешифрование: '))
    if oper == 0:
        ishod = input('Введите слово для шифрования: ')
        end = ''
        ishod_key = input('Введите ключ для шифрования: ')
        key = 0
        if ishod_key.isdigit():
            key = int(ishod_key)
        else:
            for i in ishod_key:
                key += (ord(i) - 1072)
        for i in (ishod):
            if i.isalpha():
                if i.isupper():
                    i = i.lower()
                    end += Alf[(Alf.index(i) + key) % 32].upper()
                else:
                    end += Alf[(Alf.index(i) + key) % 32]
            else:
                end += i
        print(end)
    elif oper == 1:
        end = input('Введите слово для дешифрования: ')
        ishod = ''
        ishod_key = input('Введите ключ для дешифрования: ')
        key = 0
        if ishod_key.isdigit():
            key = int(ishod_key)
        else:
            for i in ishod_key:
                key += (ord(i) - 1072)
        for i in (end):
            if i.isalpha():
                if i.isupper():
                    i = i.lower()
                    ishod += Alf[(Alf.index(i) - key) % 32].upper()
                else:
                    ishod += Alf[(Alf.index(i) - key) % 32]
            else:
                ishod += i
        print(ishod)
    else:
        break
