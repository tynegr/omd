# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Она взяла в лапку свой яркий зонтик, который сама раскрасила, '
          'и направилась в местный бар, где отлично провела время,'
          ' весело беседуя с друзьями-пернатыми, '
          'не смотря на разбушивавшийся на улице ливень.')


def step2_no_umbrella():
    print('Она направилась в местный бар, не подумав взять зонтик, '
          'и вскоре столкнулась'
          ' с безжалостным дождем, из-за которого она промокла до нитки.'
          ' Однако крепкий алгоколь и хорошая компания '
          'не позволили утке заболеть.')


if __name__ == '__main__':
    step1()
