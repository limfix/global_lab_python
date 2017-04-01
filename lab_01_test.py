# -*- coding: utf-8 -*-
import math #импорт библиотеки математических вычислений
import stud_lib #импорт созданной вручную библиотеки

X = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
A = [] #объявление пустого целочисленного массива
B = [] #объявление массива с числами после запятой
i = 0 #счётчик
j = 0
print('1 - перевод с системы счисления n в систему счисления m')
print('2 - представление двоичного кода в прямом, обратном и дополнительном')
choice = input()
if choice == '1':
    print('Введите по порядку:')
    print('Из какой системы счисления нужно конвертировать число? (2-16)')
    input_system = input()
    print('В какую систему нужно конвертировать число? (2-16)')
    output_system = input()
    print('Введите строку text, которая конвертируется в массив A:')
    text = input()

    stud_lib.create_array(A,B,text)

    k = int(input_system)

    while k < int(len(X)):
        del X[k]
        continue

    if stud_lib.checkalph(A,X) == True:
        print('Символы введённой строки входят в массив Х')
        result = stud_lib.convert(input_system,output_system,text)
        print(result)
    else:
        print('Символы введённой строки не входят в массив Х. Попробуйте снова')

elif choice == '2':
    print('Введите число в диапазоне от [-128;127]')
    k = input()
    if ((int(k) > 127) or (int(k) < -128)):
        print('Число выходит из границ диапазона')
    else:
        pos_code, neg_code, add_code = stud_lib.init_code(k)
        print('Пложительное число: ',pos_code)
        print('Обратный код: ',neg_code)
        print('Дополнительный код: ',add_code)
else:
    print('Некорректный вариант выбора, программа остановлена')
    quit()
