import random

def actions(player='player', computer='computer'):
    action_list = ['камень', 'ножницы', 'бумага']
    values = {'камень': 'ножницы', 'ножницы': 'бумага', 'бумага': 'камень'}

    def user_action():
        user_choice = input(f'\n1 - камень\n2 - ножницы \n3 - бумага\nТвой выбор, {player}: ')
        try:
            user_choice = int(user_choice) - 1
        except:
            print('Не верный ввод!')
            return user_action()
        if 0 <= user_choice <= 2:
            return action_list[user_choice]
        else:
            print('Не верный ввод!')
            return user_action()
        print(f'{player} выбрал {user_choice}')

    user_action = user_action()
    print(f'\n{player} выбрал {user_action}')

    def computer_action():
        computer_choice = random.choice(action_list)
        if computer_choice == user_action:
            return computer_action()
        else:
            return computer_choice

    computer_action = computer_action()
    print(f'{computer} выбрал {computer_action}')

    if values[user_action] == computer_action:
        return player
    else:
        return computer

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if self.is_alive():
            other.health -= self.attack_power
            print(f'{self.name} даёт леща {other.name} и наносит {self.attack_power} урона. У бедняги осталось '
                  f'{other.health} здоровья')
        else:
            print(f'{self.name} решил сдаться, у него голова уже болит.')

    def is_alive(self):
        return self.health > 0  # В данном случае вернётся булевое значение

class Game:
    def __init__(self, player_name='Игрок', computer_name='Компьютер'):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            winner = actions(self.player.name, self.computer.name)
            if winner == self.player.name:
                self.player.attack(self.computer)
            else: self.computer.attack(self.player)
        else:
            if not self.player.is_alive(): self.player.attack(self.computer)

game = Game('Иван', 'Надмозг')
game.start()