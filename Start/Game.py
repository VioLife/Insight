#Создайте программу для игры в ""Крестики-нолики"".

print("*" * 5, " Игра Крестики-нолики для двух игроков ", "*" * 5)

field = list(range(1,10))

def draw_board(field):
   print("-" * 13)
   for i in range(3):
      print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
      print("-" * 13)

def take_input(player_move):
   value = False
   while not value:
      player_answer = input("Куда поставим " + player_move+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Повторите попытку ввода числа")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(field[player_answer-1]) not in "XO"):
            field[player_answer-1] = player_move
            value = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(field):
   win_position = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_position:
       if field[each[0]] == field[each[1]] == field[each[2]]:
          return field[each[0]]
   return False

def main(field):
    counter = 0
    win = False
    while not win:
        draw_board(field)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(field)
           if tmp:
              print(tmp, "Ура! Вы победитель!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(field)
main(field)

input("Нажмите Enter для выхода!")
