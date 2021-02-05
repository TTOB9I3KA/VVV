
def шифр(str, key):
    en_st = ""
    for letter in str:
        en_st += chr(ord(letter) ^ key)
    return en_st


def crypt():
    line = input('Введите слово(предложение) которое вы бы хотели зашифровать: ')
    key = int(input("Введите ключ шифрования: "))
    encr_line = шифр(line, key)
    print("Введенная строка ", line)
    print("Зашифрованное слово:  ", encr_line)


def recrypt():

    encr_line = input('Введите слово(предложение) которое вы бы хотели разшифровать: ')
    key = int(input("Введите ключ шифрования: "))
    print("Введенная строка ", encr_line)
    encr_line = шифр(encr_line, key)
    print("Разшифрованное слово:  ", encr_line)

def opt():
    op = int(input("0. Зашифровать строку\n1. Расшифровать строку\nop(0,1): "))
    if op == 0:
        print("_______________ЗАШИФРОВКА")
        crypt()
    elif op == 1:
        print("_______________РАСШИФРОВКА")
        recrypt()
    else:
        print("Вы ввели неверное значение.")
if __name__ == "__main__":
    opt()

