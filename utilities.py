import pygame
pygame.init()


def get_percentage(now, full):
    return now/full * 100


def play_audio(audio):
    if '.mp3' not in audio:
        audio = audio + '.mp3'
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    pygame.event.wait()


def read_int(msg, errormsg = 'ERROR, try again', min = 0, max = 0):
    while True:
        while True:
            try:
                num = int(input(msg))
            except:
                print(errormsg)
            else:
                break
        if max != 0:
            if num <= max and num >= min:
                break
            else:
                print(errormsg)
    return num


def show_line():
    print('-=-' * 10)


def headline(msg):
    print('-=-'*10)
    print(msg.center(30))
    print('-=-' * 10)


def menu():
    from random import randint
    while True:
        show_line()
        print('''[1] PLAY
[2] SELECT MUSIC
[3] CREDITS
[4] QUIT''')
        show_line()
        menu_choice = read_int('Your choice: ', min = 1, max = 4)
        if menu_choice == 1:
            break
        elif menu_choice == 2:
            while True:
                show_line()
                print('''[1] Return
[2] Demons - Imagine Dragons
[3] Midnight City - M83
[4] BALENCIAGA - Halsey, $ina
[5] Random''')
                show_line()
                music_choice = read_int('Your choice: ', min = 1, max = 5)
                if music_choice == 5:
                    music_choice = randint(2, 4)
                musics = ['demons', 'midnight_city', 'balenciaga']
                if music_choice == 1:
                    break
                else:
                    play_audio(musics[music_choice-2])
        elif menu_choice == 3:
            show_line()
            print('''Code/Game - Daniel Martone
SoundTrack - Imagine Dragons, Halsey, $ina, M83
Thanks to Gustavo Guanabara from CursoEmVideo for teaching me

212 lines of code
4   hours of work
5   files (2 .py, 3 .mp3)
[1] Return''')
            show_line()
            credits_choice = read_int('Your choice: ', min = 1, max = 1)
        elif menu_choice == 4:
            show_line()
            print('Thanks for playing!')
            show_line()
            exit()


def select_difficulty():
    show_line()
    print('''[1] Easy
[2] Medium
[3] Hard
[4] Impossible
[5] (Literally) Impossible''')
    show_line()
    difficulty_choice = read_int('Your choice: ', min = 1, max = 5)
    options = [('Easy', 700),
               ('Medium', 900),
               ('Hard', 1100),
               ('Impossible', 1400),
               ('(Literally) Impossible', 2000)]

    return options[difficulty_choice-1]
