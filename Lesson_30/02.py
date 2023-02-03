import hashlib
from colorama import Fore

def write_log_pass(file_name: str, dictionary):
    with open(file_name, 'w+') as f:
        for k, v in dictionary.items():
           f.write(f'{k} {v}\n')
    f.close()

def read_log_pass(file_name: str):
    log_pass_dict = {}
    with open(file_name, encoding='utf-8') as f:
       for line in f:
           (key, val) = line.split()
           log_pass_dict[key] = val
    return log_pass_dict

log_reg = input('Для реєстрації натисніть "1"\n'
                'Для входу натисніть "0"\n'
                '> ')

def sign_up():
    while True:
        reg_login = input(Fore.GREEN + 'Введіть логін: ')
        if reg_login in hash_table_pass:
            print(Fore.RED + "Користувач з таким ім'ям вже зареєстрований. Оберіть інший логін.")
        else:
            while True:
                pass_check_1 = input(Fore.GREEN + 'Введіть пароль: ')
                pass_check_2 = input(Fore.GREEN + 'Повторіть пароль: ')
                if pass_check_1 == pass_check_2:
                    pass_hash = hashlib.md5(pass_check_1.encode())
                    hash_table_pass[reg_login] = pass_hash.hexdigest()
                    print(Fore.GREEN + '(⊃｡•́‿•̀｡)⊃ ━☆ﾟ.*･｡ﾟ\n'
                                       'Реєстрацію завершено.')
                    write_log_pass('log_pass.txt', hash_table_pass)
                    break
                else:
                    print(Fore.RED + 'Паролі не співпадають. Спробуйте ще раз')
            break

def sign_in():
    while True:
        login = input(Fore.GREEN + 'Введіть логін: ')
        if login in hash_table_pass:
            count = 0
            while True and count < 3:
                count += 1
                password = input(Fore.GREEN + 'Введіть пароль: ')
                pass_hash = hashlib.md5(password.encode())
                if hash_table_pass[login] != pass_hash.hexdigest():
                    if count != 3:
                        print(Fore.RED + f'Неправильний пароль. Спробуйте ще раз. Залишилось {3 - count} спроб.')
                    else:
                        print(Fore.RED + '彡ﾟ◉ ω◉ )つー☆*\n'
                              'Неправильний пароль. У доступі відмовлено.')
                        break
                else:
                    print(Fore.GREEN + '(⊃｡•́‿•̀｡)⊃ ━☆ﾟ.*･｡ﾟ\n'
                          'Доступ відкрито.')
                    break
            break
        else:
            print(Fore.RED + 'Невідомий логін. Спробуєте ще?')
            choice = input('Натисніть "1", якщо так.\n'
                           'Натисніть "0", якщо ні.\n'
                           '> ')
            if choice == "1":
                continue
            elif choice == "0":
                print(Fore.GREEN + '(⊃｡•́‿•̀｡)⊃ ━☆ﾟ.*･｡ﾟ\n'
                      'Сесію завершено.')
                break
            else:
                print(Fore.RED + '彡ﾟ◉ ω◉ )つー☆*\n'
                      'Невідомий значення. Сесію завершено.')
                break


hash_table_pass = read_log_pass('log_pass.txt')

if log_reg == "1":
    print()
    sign_up()
elif log_reg == "0":
    print()
    sign_in()
else:
    print(Fore.RED + "彡ﾟ◉ ω◉ )つー☆*\n"
          "Введено неправильне значення.")