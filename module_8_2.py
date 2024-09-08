def  personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in numbers:
             try:
                 result += i
             except UnboundLocalError:
                 print(f'Некорректный тип данных для подсчёта суммы - {numbers}')
                 incorrect_data += 1

             except TypeError:
                 print(f'Некорректный тип данных для подсчёта суммы - {i}')
        return [result,incorrect_data]
    except  TypeError:
        return None

def calculate_average(numbers):
    col_numbers = 0
    sr_ar = 0

    try:
        for i in numbers:
            try:
                if int(i) == i:       #
                    col_numbers += 1  #
                else:
                    continue

            except  ValueError:
                continue
            except UnboundLocalError:
 #               print(f'Некорректный тип данных для подсчёта суммы - {numbers} ')

                return None
    except  TypeError:
        print(f'В {numbers} записан некорректный тип данных')
        return None
    try :
        sum1 = personal_sum(numbers)
        if sum1 == None:
            pass
        else:
            sr_ar = sum1[0] / col_numbers
    except ZeroDivisionError:
        return 0

    return sr_ar




print(f'Результат 1: {calculate_average('1, 2, 3')}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
