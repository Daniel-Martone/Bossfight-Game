from utilities import *
from math import floor
from random import randint
from time import sleep
# █░


class Every:
    def __init__(self, starting_health):
        self.starting_health = starting_health
        self.health = starting_health
    # ----------------------
    def attack(self, damage, target):
        target.health -= damage


class Boss(Every):
    # ----------------------
    def show_life(self):
        percentage = get_percentage(self.health, self.starting_health)
        print(f'{percentage:.2f}%'.center(30))
        print('0 - ', end='')
        show = floor(percentage / 10) * 2
        print('█'*show, end='')
        print('░'*(20 - show), end='')
        print(f' - {self.starting_health}')
        print('Ʌ'.center(30))
        print('|'.center(30))
        print(f'{self.health}hp'.center(30))


class Player(Every):
    def select_attack(self):
        atk1 = randint(50, 150)
        percent1 = randint(70, 95)
        atk2 = randint(120, 210)
        percent2 = randint(40, 69)
        atk3 = randint(210, 420)
        percent3 = randint(18, 39)
        show_line()
        print(f'''[1] {percent1}% of giving {atk1} damage to the boss
[2] {percent2}% of giving {atk2} damage to the boss
[3] {percent3}% of giving {atk3} damage to the boss''')
        show_line()
        attack_choice = read_int('Your choice: ', min = 1, max = 3)
        if attack_choice == 1:
            chance = randint(1, 100)
            if percent1 > chance:
                return atk1
            else:
                return 0
        if attack_choice == 2:
            chance = randint(1, 100)
            if percent2 > chance:
                return atk2
            else:
                return 0
        if attack_choice == 3:
            chance = randint(1, 100)
            if percent3 > chance:
                return atk3
            else:
                return 0


# Loop
while True:
    # Menu
    menu()
    difficulty, boss_health = select_difficulty()
    player = Player(1000)
    boss = Boss(boss_health)
    del(boss_health)

    # Game loop
    while True:
        sleep(1.5)
        if player.health == 0:
            result = 'LOST'
            if boss.health == 0:
                result = 'WON'
            break
        if boss.health == 0:
            result = 'WON'
            break
        boss.show_life()
        damage = player.select_attack()
        player.attack(damage, boss)
        if damage == 0:
            print('YOU MISSED!')
        else:
            print('YOU HIT THE BOSS')
        sleep(1.5)
        damage = randint(60, 130)
        boss.attack(damage, player)
        if player.health < 0:
            player.health = 0
        if boss.health < 0:
            boss.health = 0
        print(f'The boss gave you {damage} damage')
        print(f'You now have {player.health}hp')
    headline(f'YOU {result}')
    sleep(1)
