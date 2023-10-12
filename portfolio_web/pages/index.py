import reflex as rx

from portfolio_web.components.boton_contacto import boton_contacto
from portfolio_web.components.boton_descarga import boton_descarga
from portfolio_web.utilitys.delta_time import delta_time
from portfolio_web.components.box_link import box_link


p1 = rx.box(rx.text('Hola, soy:', color='white'),
            rx.text('Juan Pablo', as_='b', color='#BAD9D6', fontSize='6xl'),
            rx.text('Ingeniero &', color='white', fontSize='xl'),
            rx.text('Cientifico de datos JR', color='white', fontSize='xl')
            )


bio = rx.box(rx.text('Profesional data-driven orientado a la '
                     'resolución de problemas mediante innovación continua'),
             rx.divider(width=0),
             rx.text(f'Desde hace {delta_time("2022-08-19")} trabajo como ingeniero '
                     f'en el departamento tecnico de una empresa local realizando diferentes'
                     f'tareas orientadas a la gestion de proyectos e innovacion de equipos y procesos'
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
                                boton_descarga,
                                boton_contacto,
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

p3 = rx.stack(box_link('Proyectos Github',
                       '/projects'),
              box_link('Experiencia',
                       'experience'),
              direction='row',
              height='100%')

index = rx.box(
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
    rx.flex(rx.box(p3, bg='#224040', width='100%'),
            height='15%', ),
    width='100%',
    h='100vh'

)


def index_page():
    return rx.box(
        # navbar(),
        # rx.divider(),
        index,
        min_width='100%',
    )
