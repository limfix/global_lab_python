import math

def init_code(A):
    if A[0] == '-':
        negative_number = True
        new_string = A.replace('-','')
        new_number = math.fabs(int(new_string))
    else:
        negative_number = False
        new_number = int(A)
    X = []
    i = 0
    while new_number >= 0:
        i += 1
        if new_number == 3:
            X.append('1')
            X.append('1')
            break
        elif new_number == 2:
            X.append('0')
            X.append('1')
            break
        rest = int(new_number) % 2
        X.append(str(rest))
        new_number = int(new_number / 2)

    X.reverse()
    t = 0
    while t < (6 - i):
        X.append('0')
        t += 1
    X.reverse()
    X.append('0')
    X.reverse()
    positive_code = ''.join(X)
    if negative_number == True:
        edit_string = positive_code
        negative_code = edit_string.replace('0','null')
        negative_code = negative_code.replace('1','one')
        negative_code = negative_code.replace('null','1')
        negative_code = negative_code.replace('one','0')

        #рассчёт для addicted_number

        X = []
        i = 0
        addicted_number = math.fabs(int(A)) - 1
        while addicted_number >= 0:
            i += 1
            rest = int(addicted_number) % 2
            X.append(str(rest))
            addicted_number = int(addicted_number / 2)
            if addicted_number == 0:
                X.append('0')
                break
            elif addicted_number == 1:
                X.append('1')
                break
        t = 0
        while t < (6 - i):
            X.append('0')
            t += 1
        X.append('0')
        X.reverse()
        addicted_code = ''.join(X)
        edit_addicted_string = addicted_code
        negative_addicted_code = edit_addicted_string.replace('0','null')
        negative_addicted_code = negative_addicted_code.replace('1','one')
        negative_addicted_code = negative_addicted_code.replace('null','1')
        negative_addicted_code = negative_addicted_code.replace('one','0')
        return positive_code, negative_code, negative_addicted_code
    else:
        negative_code = positive_code
        addicted_code = positive_code
        return positive_code, negative_code, addicted_code

def checkalph(A,X):
    IsAlphTrue = False
    i = 0 #обнуление счётчиков
    j = 0
    count_same_liters = 0 # новый счётчик, подсчитывающий общее количество вхождений

    c_one = len(A) - 1 # переменные для цикла перебора элементов массива А на наличие в Х
    c_two = len(X) - 1

    while i <= c_one:
        while j <= c_two:
            if A[i] == X[j]: # если элементы совпадают
                IsAlphTrue = True
                del A[i] # удалить символ из массива
                c_one =- 1 # уменьшить значение длины массива на 1
                if len(A) == 0: # если массив А пуст, завершить цикл
                    break
                else:
                    i = 0 # если же нет, обнулить счётчики и перейти к началу общего цикла
                    j = 0
                    continue
            else: # если элементы не совпадают
                j += 1  # увеличить значение j на 1 (если программа проверяла символ A[i] на совпадение с элементом '0', то
                        # теперь будет проверять на совпадение с элементом '1')
                if j > c_two: # если ни один элемент массива X не подошёл, тогда прерывание цикла
                    IsAlphTrue = False
                    break
                else:
                    continue
        break

    return IsAlphTrue

def create_array(integer_array,float_array,input_text):
    i = 0
    dots_count = 0
    while i < len(input_text): # цикл перебора от 0 до n (n - длина введенной пользователем строки из переменной "text")
        if input_text[i] == '.':
            dots_count += 1
            i += 1
            break
        else:
            integer_array.append(input_text[i]) # в массив А добавляется очередной элемент i из строки "text"
            i += 1 # увеличение счётчика на 1
    while i < len(input_text):
        float_array.append(input_text[i])
        i += 1

def convert(var_input,var_output,text):
    integer_array = []
    float_array = []
    dots_count = 0
    result = 0
    result_integer = 0
    result_float = 0
    j = 0
    for i in range(len(text)):
        if text[i] == '.':
            dots_count += 1
    if dots_count > 1:
        error_message = 'Неверный формат числа. Попробуйте снова'
        return error_message
    elif dots_count != 0:
        for i in range(len(text)):
            if (text[i] == 'A'):
                integer_array.append(10)
            elif (text[i] == 'B'):
                integer_array.append(11)
            elif (text[i] == 'C'):
                integer_array.append(12)
            elif (text[i] == 'D'):
                integer_array.append(13)
            elif (text[i] == 'E'):
                integer_array.append(14)
            elif (text[i] == 'F'):
                integer_array.append(15)
            elif (text[i] == '.'):
                j = i + 1
                break
            else:
                integer_array.append(int(text[i]))

        for i in range(j,len(text)):
            if (text[i] == 'A'):
                float_array.append(10)
            elif (text[i] == 'B'):
                float_array.append(11)
            elif (text[i] == 'C'):
                float_array.append(12)
            elif (text[i] == 'D'):
                float_array.append(13)
            elif (text[i] == 'E'):
                float_array.append(14)
            elif (text[i] == 'F'):
                float_array.append(15)
            else:
                float_array.append(int(text[i]))

        float_array.reverse()


        #перевод в десятичную до точки
        for i in range(len(integer_array)):
            last_number = integer_array.pop()
            result_integer += last_number * int(var_input)**i


        #перевод в произвольную до точки
        global_integer_array = []
        new_number = int(result_integer)
        while new_number >= 0:                                          ###
            rest = int(new_number) % int(var_output)
            if (rest == 10):
                global_integer_array.append('A')
            elif (rest == 11):
                global_integer_array.append('B')
            elif (rest == 12):
                global_integer_array.append('C')
            elif (rest == 13):
                global_integer_array.append('D')
            elif (rest == 14):
                global_integer_array.append('E')
            elif (rest == 15):
                global_integer_array.append('F')
            else:
                global_integer_array.append(str(rest))
            new_number = int(new_number / int(var_output))
            if int(new_number) < (int(var_output)):
                if (new_number == 10):
                    global_integer_array.append('A')
                elif (new_number == 11):
                    global_integer_array.append('B')
                elif (new_number == 12):
                    global_integer_array.append('C')
                elif (new_number == 13):
                    global_integer_array.append('D')
                elif (new_number == 14):
                    global_integer_array.append('E')
                elif (new_number == 15):
                    global_integer_array.append('F')
                else:
                    global_integer_array.append(str(new_number))
                break

        #перевод в десятичную после точки
        len_float_array = len(float_array)
        for i in range(len(float_array)):
            last_number = float_array.pop()
            result_float += last_number * int(var_input)**(-(i))
        result_float = round(result_float * 10**(-1),len_float_array)


        #перевод в произвольную после точки
        global_float_array = []
        new_number = round(float(result_float)*int(var_output),len_float_array)
        for i in range(10):
            if new_number >= 1:
                if (int(new_number) == 10):
                    global_float_array.append('A')
                    new_number -= 10
                elif (int(new_number) == 11):
                    global_float_array.append('B')
                    new_number -= 11
                elif (int(new_number) == 12):
                    global_float_array.append('C')
                    new_number -= 12
                elif (int(new_number) == 13):
                    global_float_array.append('D')
                    new_number -= 13
                elif (int(new_number) == 14):
                    global_float_array.append('E')
                    new_number -= 14
                elif (int(new_number) == 15):
                    global_float_array.append('F')
                    new_number -= 15
                else:
                    global_float_array.append(str(int(new_number)))
                    new_number -= int(new_number)
            else:
                global_float_array.append('0')
            new_number = round(float(new_number)*int(var_output),len_float_array)
        dot_array = ['.']
        global_integer_array.reverse()
        global_array = global_integer_array + dot_array + global_float_array
        global_arrayString = ''.join(global_array)
        return global_arrayString

    #условие для целого числа (кол-во точек = 0)
    else:
        for i in range(len(text)):
            if (text[i] == 'A'):
                integer_array.append(10)
            elif (text[i] == 'B'):
                integer_array.append(11)
            elif (text[i] == 'C'):
                integer_array.append(12)
            elif (text[i] == 'D'):
                integer_array.append(13)
            elif (text[i] == 'E'):
                integer_array.append(14)
            elif (text[i] == 'F'):
                integer_array.append(15)
            else:
                integer_array.append(int(text[i]))
        i = 0
        for i in range(len(integer_array)):
            last_number = integer_array.pop()
            result += last_number * int(var_input)**i
        global_array = []
        new_number = int(result)
        while new_number >= 0:
                rest = int(new_number) % int(var_output)
                if (rest == 10):
                    global_array.append('A')
                elif (rest == 11):
                    global_array.append('B')
                elif (rest == 12):
                    global_array.append('C')
                elif (rest == 13):
                    global_array.append('D')
                elif (rest == 14):
                    global_array.append('E')
                elif (rest == 15):
                    global_array.append('F')
                else:
                    global_array.append(str(rest))
                new_number = int(new_number / int(var_output))
                if int(new_number) < (int(var_output)):
                    if (new_number == 10):
                        global_array.append('A')
                    elif (new_number == 11):
                        global_array.append('B')
                    elif (new_number == 12):
                        global_array.append('C')
                    elif (new_number == 13):
                        global_array.append('D')
                    elif (new_number == 14):
                        global_array.append('E')
                    elif (new_number == 15):
                        global_array.append('F')
                    else:
                        global_array.append(str(new_number))
                    break
        global_array.reverse()
        global_arrayString = ''.join(global_array)
        global_arrayString = round(int(global_arrayString))
        return global_arrayString

def init_double_code(A):
    negative_number = False
    i = 0
    X = []

    if A[0] == '1':
        negative_number = True
        while negative_number == True:
            editing_code = A
            edit_addicted_string = editing_code
            negative_code = edit_addicted_string.replace('0','null')
            negative_code = negative_code.replace('1','one')
            negative_code = negative_code.replace('null','1')
            negative_code = negative_code.replace('one','0')
            while i < len(negative_code):
                if A[i] == '.':
                    i += 1
                    continue
                else:
                    X.append(A[i])
                    i += 1
            X.reverse()
            i = 0
            j = 0
            total_count = len(X)
            X[0] = int(X[0]) + 1
            while i < len(X):
                while j < len(X):
                    if( (j == (len(X) - 1)) and (int(X[j]) == 2) ):
                        X.append(1)
                        X[j] = 0
                        break
                    elif int(X[j]) == 2:
                        X[j] = 0
                        X[j+1] = int(X[j+1]) + 1
                    j += 1
                if i > total_count:
                    break
                i += 1
            i = 0
            while i < len(X):
                X[i] = str(X[i])
                i += 1
            X.reverse()
            addicted_code = ''.join(X)
            return addicted_code, negative_code
    elif A[0] == '0':
        negative_number = False
        addicted_code = A
        negative_code = A
        return addicted_code, negative_code
    else:
        print('Error')
        quit()

def convert_neg_code(neg_code):
    negative_number = False
    X = []
    Y = []
    i = 1
    if neg_code[0] == '1':
        negative_number = True
    if negative_number == True:
        while i < len(neg_code):
            X.append(str(neg_code[i]))
            i += 1
        X = ''.join(X)
        X = convert(2,10,X)
        i = 0
        X = str(X)
        while i < len(X):
            Y.append(X[i])
            i += 1
        Y.reverse()
        Y.append('-')
        Y.reverse()
        Y = ''.join(Y)
        return Y
    elif negative_number == False:
        while i < len(neg_code):
            X.append(str(neg_code[i]))
            i += 1
        X = ''.join(X)
        X = convert(2,10,X)
        return X


def sum_neg_code(neg_code_one,neg_code_two,count_rank):
    negative_limit = -(2**(int(count_rank)))+1
    positive_limit = 2**(int(count_rank))
    neg_code_one = int((convert_neg_code(neg_code_one)))
    neg_code_two = int((convert_neg_code(neg_code_two)))
    integer_result = neg_code_one + neg_code_two
    error_message = 'Разрядная сетка переполнена. Введите корректное значение'
    X = []
    i = 0
    if( neg_code_one or neg_code_two ) > positive_limit:
        return error_message
    elif( neg_code_one or neg_code_two ) < negative_limit:
        return error_message
    elif ((integer_result > positive_limit) or (integer_result < negative_limit)):
        return error_message
    else:
        return integer_result
