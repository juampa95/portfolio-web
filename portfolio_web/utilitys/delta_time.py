from datetime import datetime


def delta_time(desde):
    dif = datetime.now() - datetime.strptime(desde, "%Y-%m-%d")
    anios = int(dif.days / 365)
    meses = int(dif.days % 365) // 30
    if anios == 0:
        if meses == 0:
            return 'nada'
        elif meses == 1:
            return f'{meses} mes'
        else:
            return f'{meses} meses'
    elif anios == 1:
        if meses == 0:
            return f'{anios} año'
        elif meses == 1:
            return f'{anios} año y {meses} mes'
        else:
            return f'{anios} año y {meses} meses'
    else:
        if meses == 0:
            return f'{anios} años'
        elif meses == 1:
            return f'{anios} años y {meses} mes'
        else:
            return f'{anios} años y {meses} meses'
