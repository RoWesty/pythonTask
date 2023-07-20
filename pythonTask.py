import re
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

print("------------------------------------------------------------------------------------------")
text = input("Введите предложение: ")
words = re.findall(r"[\w']+", text) # r"[\w']+" я понимаю какую функцию она выполняет, но не знаю как, просьба если прочитаете напишите.
for i in reversed(range(len(words))):
    if (i % 2):
        None
    else:
        del words[i]
print(f'Все четные значения: {words}')

print("-----------------------------------------------------------------------------------------")
text = input("Введите предложение: ")
words = re.findall(r"[\w']+", text)
result = []
for word in words:
    chartext = re.split("",word.lower())
    charvowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"] # Стоит ли вообще что-то писать? 
    vowels = []
    for i in chartext:
        for j in charvowels:
            if i == j:
                vowels.extend(i)
                for count, i in enumerate(range(0, len(vowels))):
                     if i >= 2:
                         result.append(word)
print(f'Все слова с 3 или более гласными буквами: {result}')

print("-----------------------------------------------------------------------------------------")
Numbers = input("Введите цифры: ")
Number = re.findall(r"[\w']+", Numbers)
ConvertNumber = list(map(int, Number)) # Стоит ли вообще что-то писать? 
ConvertNumber.sort()
print(f'Второй по величине элемент в списке: {ConvertNumber[-2]}')

print("------------------------------------------------------------------------------------------")
Numbers = input("Введите цифры: ")
Number = re.findall(r"[\w']+", Numbers) # Стоит ли вообще что-то писать? 
ConvertNumber = list(map(int, Number))
result = list(set(ConvertNumber))
print(f'Дубликаты уничтожены, итоговый список: {result}')

print("-------------------------------------------------------------------------------------------")
print("Выберите необходимый вам csv файл")
Tk().withdraw()
filename = askopenfilename()
with open(filename, encoding='utf-8') as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        # Вывод строк
        print(f' {row["Имя"]}, {row["Пол"]}', end='')
        print(f' , {row["Возраст"]}, {row["Заработная плата"]}')
        count += 1
    print(f'Всего в файле {count + 1} строк.')

print("------------------------------------------------------------------------------------------")
words = input("Введите предложение:")
length = len(words)
for i in range(length - 2):
    for j in range(i + 3, length + 1):
        substring = words[i:j]
        print(substring)
