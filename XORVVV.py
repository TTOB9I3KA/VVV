message = input("Введите зашифрованный текст или обычный текст: ")
key = input("Введите ключ для шифрования или дешифрования: ")
long = len(message)
result = ""

for i in range(long):
    current = message[i]
    current_key = key[i%len(key)]
    result += chr(ord(current) ^ ord(current_key))

print ("Результат: ", result)
print('Конец программы!')
input('Напишите отзыв о программе')
