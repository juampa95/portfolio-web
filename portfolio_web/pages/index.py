import reflex as rx
from datetime import datetime

from portfolio_web.base_state import State
from portfolio_web.components.navbar import navbar
from portfolio_web.styles import styles

top_box = rx.flex(rx.square('',
                            bg='black',
                            width='70%'),
                  rx.square('',
                            bg='green',
                            width='30%'),
                  h='300px'
                  )

grilla = rx.grid(
    rx.grid_item(row_span=2, col_span=14, bg='#224040',),
    rx.grid_item(row_span=2, col_span=6, bg='#BAD9D6',),
    rx.grid_item(row_span=6, col_span=12, bg='#224040', ),
    rx.grid_item(rx.flex(rx.box('',bg='#224040',h='100%', width='50%'),
                         rx.box('',bg='#BAD9D6',h='100%', width='50%'),
                         rx.flex(rx.image(src='/perfil.png'),
                                 align='end',
                                 justify='center',
                                 position='absolute',
                                 width='100%'),
                        align='end',
                        height='100%',
                        position='relative'),
                 row_span=6, col_span=4 ,
                 ),
    rx.grid_item(row_span=6, col_span=4, bg='#BAD9D6', ),
    rx.grid_item(row_span=8, col_span=20, bg='#345959',),
    rx.grid_item(row_span=4, col_span=20, bg='#224040',),
    template_rows="repeat(20, 1fr)",
    template_columns="repeat(20, 1fr)",
    h='100vh',
    width='100%',
    gap=0
                 )

p1 = rx.box(rx.text('Hola, soy:', color='white'),
            rx.text('Juan Pablo', as_='b', color='#BAD9D6',fontSize='6xl'),
            rx.text('Ingeniero &', color='white', fontSize='xl'),
            rx.text('Cientifico de datos JR', color='white', fontSize='xl')
            )

p2 = rx.hstack(rx.box(rx.image(src='/perfilcfondo.png'),
                   width='30%', align='center', justify='center'),
               rx.card('el texto del about me',
                       header=rx.text('About Me'),
                       footer=rx.text('Boton de CV y email'),
                       bg='#345959'),
               )

flex = rx.box(
    rx.flex(rx.flex(p1, bg='#224040', h='100%', width='70%', align='center', justify='center'),
            rx.box(bg='#BAD9D6', h='100%', width='30%'),
            rx.flex(rx.image(src='/perfil.png'),
                    align='end',
                    position='absolute',
                    width='30%',
                    left='56%'),
            align='end',
            height='40%',
            width='100%',
            position='relative'),
    rx.flex(rx.flex(p2,bg='#345959', width='100%'),
            height='40%'),
    rx.flex(rx.box(bg='#224040', width='100%'),
            height='20%',),
    width='100%',
    h='100vh'

)


def index_page():
    return rx.box(
        # navbar(),
        # rx.divider(),
        flex,
        min_width='100%',
        # bg='#224040',
    )