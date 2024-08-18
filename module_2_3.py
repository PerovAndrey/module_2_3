# while 1 > 0:
#     number = int(input('Введите число: '))
#     if number % 2 == 0:
#         print('Число четное')
#         continue
#     else:
#         print('Число нечетное')
#     print('Меня не забыли')
# print('Я за циклом')

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    current_element = my_list[a]
    if current_element < 0:
        break
    if current_element == 0:
        a += 1
        continue
    print(current_element)
    a += 1