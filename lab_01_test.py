# -*- coding: utf-8 -*-
import math #импорт библиотеки математических вычислений
import stud_lib #импорт созданной вручную библиотеки

X = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
A = [] #объявление пустого целочисленного массива
B = [] #объявление массива с числами после запятой
i = 0 #счётчик
j = 0
first_choice_process = False
print('1 - перевод с системы счисления n в систему счисления m')
print('2 - представление десятичного кода в прямом, обратном и дополнительном двоичном коде')
print('3 - представление двоичного кода в прямом, обратном и дополнительном двоичном коде')
print('4 - прибавление/отнимание двоичных чисел в обратном коде')
choice = input()

if choice == '1':
    first_choice_process = True
    while(first_choice_process == True):
        print('Введите по порядку:')
        print('Из какой системы счисления нужно конвертировать число? (2-16)')
        input_system = input()
        if( (int(input_system) > 16) or (int(input_system) < 2) ):
            print('Некорректная система счисления (>16 или <2)')
            continue
        else:
            print('В какую систему нужно конвертировать число? (2-16)')
            output_system = input()
            if( (int(output_system) > 16) or (int(output_system) < 2) ):
                print('Некорректная система счисления (>16 или <2)')
                continue
            else:
                print('Введите строку text, которая конвертируется в массив A:')
                text = input()
                break

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

elif choice == '3':
    print('Введите двоичный код (в диапазоне [0000 0000;1111 1111])')
    X = input()
    negative_code, addicted_code = stud_lib.init_double_code(X)
    print('Обратный код: ', negative_code)
    print('Дополнительный код: ', addicted_code)

elif choice == '4':
    print('Программа складывает и отнимает два двоичных числа в обратном коде.')
    print('Требуется ввести по порядку два числа, где первый символ "1" или "0" указывает на знак.')
    print('1 - знак минус, 0 - знак плюс')
    h = input('Введите разрядность сетки: ')
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    result = stud_lib.sum_neg_code(a,b,h)
    print('Результат сложения в обратном коде: ', result)

else:
    print('Некорректный вариант выбора, программа остановлена')
    quit()
