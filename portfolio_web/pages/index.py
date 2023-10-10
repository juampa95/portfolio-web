import reflex as rx
from datetime import datetime, timedelta

from portfolio_web.base_state import State
from portfolio_web.components.navbar import navbar
from portfolio_web.styles import styles

p1 = rx.box(rx.text('Hola, soy:', color='white'),
            rx.text('Juan Pablo', as_='b', color='#BAD9D6', fontSize='6xl'),
            rx.text('Ingeniero &', color='white', fontSize='xl'),
            rx.text('Cientifico de datos JR', color='white', fontSize='xl')
            )


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


bio = rx.box(rx.text('Profesional data-driven orientado a la '
                     'resolución de problemas mediante innovación continua'),
             rx.divider(width=0),
             rx.text(f'Desde hace {delta_time("2022-08-19")} trabajo como ingeniero '
                     f'en el departamento tecnico de una empresa local realizando diferentes'
                     f'tareas orientadas a la gestion de proyectos e innovacion de equipos'
                     , font_size='0.8em'),
             rx.text(f'Llevo {delta_time("2021-10-10")} capacitandome en Python, Data y '
                     f'Machine-learning ', font_size='0.8em'))

p2 = rx.hstack(rx.box(rx.image(src='/perfilrecorte.png'),
                      width=['50%','40%','35%','30%','25%'],
                      display=["none", "none", "flex", "flex", "flex"],
                      boxShadow="5px 5px 10px rgba(0, 0, 0, 0.2), -5px -5px 10px rgba(11, 111, 111, 0.8)"
                      ),
               rx.container(rx.heading('About Me'),
                            rx.divider(width='15%',
                                       variant='solid'),
                            bio,
                            rx.stack(
                                rx.button('Descargar CV', bg='#BAD9D6', size='sm'),
                                rx.button('Enviar email', bg='#BAD9D6', size='sm'),
                                direction='row',
                                justify='left',
                                margin_top='1em',
                                gap=3,
                            ),
                            ),
               left=['2%','5%','10%','15%','20%'],
               position='relative',
               width=['100%','90%','80%','75%','70%'],
               display='flex',
               # min_width=["15em", "15em", "15em", "20em", "20em"]
               )

flex = rx.box(
    rx.flex(rx.flex(p1, bg='#224040', h='100%', width='70%', align='center', justify='center'),
            rx.box(bg='#BAD9D6', h='100%', width='30%'),
            rx.flex(rx.image(src='/perfil.png'),
                    align='end',
                    position='absolute',
                    width=['50%','45%','40%','35%','30%'],
                    left=['45%','48%','50%','52%','56%'],
                    display=['none','flex','flex','flex','flex']),
            align='end',
            height='40%',
            width='100%',
            position='relative'),
    rx.flex(rx.flex(p2, bg='#345959', width='100%'),
            height='45%'),
    rx.flex(rx.box(bg='#224040', width='100%'),
            height='15%', ),
    width='100%',
    h='100vh'

)


def index_page():
    return rx.box(
        # navbar(),
        # rx.divider(),
        flex,
        min_width='100%',
    )
