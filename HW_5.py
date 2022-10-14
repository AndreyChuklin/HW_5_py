'''
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''
# txt = 'Здесь есть абв, и даже много абв, абв, абв, абв. Ладно, остановимся'
# print(txt)

# txt_1 = 'А здесь уже нет абв, и даже много абв, абв, абв, абв. Ладно, остановимся'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# txt_1 = del_some_words(txt_1)
# print(txt_1)

'''
2. Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
'''
# from random import *
# import os


# text = ('Приветствую Вас! Сегодня будем играть в конфеты')
# print(text)

# message = ['Вы ходите первый']


# def player_vs_player():
#     candies_total = 2021
#     max_take = 28
#     count = 0
#     player_1 = input('\nКак твое имя?: ')
#     player_2 = input('\nИмя оппонента: ')

#     print(f'\nПора начинать игру {player_1} и  {player_2} \n')
#     print('\n Опеределим, чей первый ход будет.\n')

#     x = randint(1, 2)
#     if x == 1:
#         lucky = player_1
#         loser = player_2
#     else:
#         lucky = player_2
#         loser = player_1
#     print(f'Поздравляю {lucky}, твой ход первый!')

#     while candies_total > 0:
#         if count == 0:
#             step = int(input(f'\n{choice(message)} {lucky} = '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\n Больше {max_take} конфет брать нельзя, {lucky}, бери снова: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\n еще осталось {candies_total}')
#             count = 1
#         else:
#             print('Конфеты закончились')

#         if count == 1:
#             step = int(input(f'\n{choice(message)}, {loser} '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\n Больше {max_take} конфет брать нельзя {loser}, бери снова: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\n еще осталось {candies_total}')
#             count = 0
#         else:
#             print('Конфеты закончились')

#     if count == 1:
#         print(f'{loser} Победитель!')
#     if count == 0:
#         print(f'{lucky} Победитель!')


# player_vs_player()


# def player_vs_bot():
#     candies_total = 2021
#     max_take = 28
#     player_1 = input('\n Как твое имя?: ')
#     player_2 = 'Комп'
#     players = [player_1, player_2]
#     print(f'\n Пора начинать игру {player_1} и {player_2} \n')
#     print('\n Узнаем, кого первый ход будет\n')

#     lucky = randint(-1, 0)

#     print(f'Поздравляю {players[lucky+1]}, ты ходишь первым!')

#     while candies_total > 0:
#         lucky += 1

#         if players[lucky % 2] == 'Комп':
#             print(
#                 f'\n Ходит {players[lucky%2]} \n Еще осталось {candies_total}. \n{choice(message)}: ')

#             if candies_total < 29:
#                 step = candies_total
#             else:
#                 delen = candies_total//28
#                 step = candies_total - ((delen*max_take)+1)
#                 if step == -1:
#                     step = max_take -1
#                 if step == 0:
#                     step = max_take
#             while step > 28 or step < 1:
#                 step = randint(1,28)
#             print(step)
#         else:
#             step = int(input(f'\n Твой ход,  {players[lucky%2]} \n Остаток {candies_total} {choice(message)}:  '))
#             while step > max_take or step > candies_total:
#                 step = int(input(f'\n За ход можно взять {max_take} конфет, еще раз: '))
#         candies_total = candies_total - step

#     print(f'Остаток {candies_total} \n Победил {players[lucky%2]}')

# player_vs_bot()

'''
3. Создайте программу для игры в ""Крестики-нолики"".
'''

# desk = list(range(1,10))

# def draw_board(desk):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", desk[0+i*3], "|", desk[1+i*3], "|", desk[2+i*3], "|")
#         print ("-" * 13)

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Выбирай ячейку " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Введите верное число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(desk[player_answer-1]) not in "XO"):
#                 desk[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Эта ячейка занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(desk):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(desk)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(desk)
#             if tmp:
#                 print (tmp, "Победа!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(desk)

# main(desk)

'''
4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''
# with open('file_code.txt', 'w') as data:
#     data.write('ffffgfghhggggghhbbbbbbghjjjjjuuuyyttttt')

# with open('file_code.txt', 'r') as data:
#     string = data.readline()

# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('file_code.txt', 'r') as file:
#     decoded_string = file.read()

# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + rle_encode(decoded_string))
# print(f'Comp r: \t{round(len(decoded_string) / len(encoded_string), 1)}')

'''
5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

Входные и выходные данные хранятся в отдельных текстовых файлах.
'''