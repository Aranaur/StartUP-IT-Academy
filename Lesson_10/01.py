import sys


def month_name():
    month_dict = {
        1: 'Січень',
        2: 'Лютий',
        3: 'Березень',
        4: 'Квітень',
        5: 'Травень',
        6: 'Червень',
        7: 'Липень',
        8: 'Серпень',
        9: 'Вересень',
        10: 'Жовтень',
        11: 'Листопад',
        12: 'Грудень'
    }
    try:
        month_number = int(input('Введіть номер місяця: '))
        print(month_dict[month_number])
    except ValueError:
        print('Невідоме значення.', file=sys.stderr)
    except KeyError:
        print("Введіть натуральне число від 1 до 12.", file=sys.stderr)
    finally:
        print('-'*10)


month_name()
