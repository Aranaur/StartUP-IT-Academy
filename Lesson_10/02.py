import sys


def list_unique_check():
    try:
        my_list = [int(item) for item in input('Введіть список чисел через кому: ').split(sep=',')]
        if len(my_list) == len(set(my_list)):
            print('Всі елементи списку унікальні')
        else:
            print('Не всі елементи списку унікальні')
    except ValueError:
        print('Введено не числа', file=sys.stderr)
    except Exception as ex:
        print(ex, 'Щось пішло не по плану', file=sys.stderr)


list_unique_check()
