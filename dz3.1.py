# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
def avn(name, age, city):
    print(name, age, 'years,', 'live in', city)
avn('Alexey', 24, 'Moscow')

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
def three_number(a, b, c):
    return(max(a, b, c))
print(three_number(7, 20 ,8))

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def string_arg(*args):
    print(max(args, key=len))
stroky = []
i=0
b = '1'
while i>=0:
    if b == '1':
        a = input('введите строку: ')
        stroky.append(a)
        b = input('введите 1 если хотите продолжить вводить строки: ')
    else:
        break
    i += 1
print(stroky)
string_arg(stroky)

def string_arg(*args):
    print(max(args, key=len))
string_arg('dkfj','dkfjdk','dkfsjleik','dk')

