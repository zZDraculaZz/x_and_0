from texttable import Texttable  # pip install
import random

text = {"choose_side": "Пожалуйста введите в консоль кем будете играть: 'X' или '0'.",
        "error": "Ошибка! Попробуйте ещё раз!",
        "your_move": "Ваш ход! Выберите и впишите клетку, куда собираетесь совершить ход. "
                     "Например: '11'.",
        "game_over": "Игра завершилась!",
        "draw_win": "Ничья! Победителя нет.",
        "X_win": "Крестики победили!",
        "0_win": "Нолики победили!",
        }

moves = ["00", "01", "02",  # список доступных ходов
         "10", "11", "12",
         "20", "21", "22"]

x_table = [["-", "-", "-"],  # для удобного позиционирования клеток(используется в visual_table)
           ["-", "-", "-"],
           ["-", "-", "-"]
           ]


def display():  # красивое оформление поля
    visual_table = Texttable()
    visual_table.add_rows([["", "O", "1", "2"],
                           ["O", x_table[0][0], x_table[0][1], x_table[0][2]],
                           ["1", x_table[1][0], x_table[1][1], x_table[1][2]],
                           ["2", x_table[2][0], x_table[2][1], x_table[2][2]]])
    print(visual_table.draw())
    pass


def player_move(player):  # ход игрока на поле
    print(text["your_move"])
    move = input()
    while move not in moves:
        print(text["error"])
        move = input()
    x_table[int(move[0])][int(move[1])] = player
    moves.remove(move)
    pass


def bot_move(bot):  # ход бота на поле
    move = random.choice(moves)
    x_table[int(move[0])][int(move[1])] = bot
    moves.remove(move)
    pass


def win_combination(bot, player, winner):  # победные комбинации
    if x_table[0][0] == bot and x_table[0][1] == bot and x_table[0][2] == bot:
        winner = bot
    elif x_table[0][0] == player and x_table[0][1] == player and x_table[0][2] == player:
        winner = player
    elif x_table[1][0] == bot and x_table[1][1] == bot and x_table[1][2] == bot:
        winner = bot
    elif x_table[1][0] == player and x_table[1][1] == player and x_table[1][2] == player:
        winner = player
    elif x_table[2][0] == bot and x_table[2][1] == bot and x_table[2][2] == bot:
        winner = bot
    elif x_table[2][0] == player and x_table[2][1] == player and x_table[2][2] == player:
        winner = player
    elif x_table[0][0] == bot and x_table[1][0] == bot and x_table[2][0] == bot:
        winner = bot
    elif x_table[0][0] == player and x_table[1][0] == player and x_table[2][0] == player:
        winner = player
    elif x_table[0][1] == bot and x_table[1][1] == bot and x_table[2][1] == bot:
        winner = bot
    elif x_table[0][1] == player and x_table[1][1] == player and x_table[2][1] == player:
        winner = player
    elif x_table[0][2] == bot and x_table[1][2] == bot and x_table[2][2] == bot:
        winner = bot
    elif x_table[0][2] == player and x_table[1][2] == player and x_table[2][2] == player:
        winner = player
    elif x_table[0][0] == bot and x_table[1][1] == bot and x_table[2][2] == bot:
        winner = bot
    elif x_table[0][0] == player and x_table[1][1] == player and x_table[2][2] == player:
        winner = player
    elif x_table[0][2] == bot and x_table[1][1] == bot and x_table[2][0] == bot:
        winner = bot
    elif x_table[0][2] == player and x_table[1][1] == player and x_table[2][0] == player:
        winner = player
    else:
        pass
    return winner


def game_checking(bot, player, winner):  # проверям есть победитель или нет.
    winner = win_combination(bot, player, winner)
    if not moves and not winner:  # если не осталось ходов - ничья
        winner = "draw"
    return winner


def x_game_0():  # игра
    print(text["choose_side"])
    player = input().upper()
    while player != "X" and player != "0":
        print(text["error"], "\n" + text["choose_side"])
        player = input().upper()
    if player == "X":
        bot = "0"
    else:
        bot = "X"
    winner = ""
    while not winner:
        if player == "X":
            display()
            player_move(player)
        else:
            bot_move(bot)
        winner = game_checking(bot, player, winner)
        if winner:
            display()
            print(text["game_over"], "\n" + text[winner + "_win"])
            break
        if player == "0":
            display()
            player_move(player)
        else:
            bot_move(bot)
        winner = game_checking(bot, player, winner)
        if winner:
            display()
            print(text["game_over"], "\n" + text[winner+"_win"])


x_game_0()
