from datetime import datetime, timedelta


def chessclock():
    print('[Für Start Enter drücken]')
    input()
    time_start = datetime.now()

    while True:
        ins = input()
        if ins == '':
            time_end = datetime.now()
            dt = time_end - time_start
            delta = timedelta(seconds=dt.seconds)
            print(f'Spielzeit {delta}')


def chessclock_dual():
    time_A = timedelta()
    time_B = timedelta()
    actual_player = 'A'

    print('[Für Start Enter drücken]')
    input()
    print('Spieler A ist dran')
    time_start = datetime.now()

    while True:
        ins = input()
        if ins == '':
            time_end = datetime.now()
            dt = time_end - time_start
            playtime = timedelta(seconds=dt.seconds)
            if actual_player == 'A':
                time_A += playtime
                actual_player = 'B'
            else:
                time_B += playtime
                actual_player = 'A'
            time_start = datetime.now()
            print('Zeit Spieler A: ' + str(time_A))
            print('Zeit Spieler B: ' + str(time_B))
            print('Aktueller Spieler: ' + actual_player)


if __name__ == '__main__':
    chessclock_dual()
