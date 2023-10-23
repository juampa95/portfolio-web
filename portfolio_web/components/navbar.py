import reflex as rx
from portfolio_web.styles.colors import colors as c
color_principal = 'spectra'


def navbar():
    return rx.flex(
        rx.box(
            rx.link(
                rx.image(src='/portafolio.png',width='50px',),
                href='/aboutpage'
            ),
            padding_left='10px'
        ),
        rx.center(
            rx.menu(
                rx.menu_button('MENU',
                               as_='b',
                               ),
                rx.menu_list(
                    rx.link(
                        rx.menu_item('About'),
                                href='/aboutpage'
                    ),
                    rx.link(
                        rx.menu_item('Experience'),
                                href='/experience',
                    ),
                    rx.link(
                        rx.menu_item('Projects'),
                                href='/projects',
                    )
                )
            ),
            padding='10px'
        ),
        justify_content='space-between',
        min_width='90%',
        border_radius='10px',
        bg='black'
    )

def breadcrumb_item(name: str, href :str, current :bool):
    if current:
        item = rx.center(rx.text(name,
                                 font_size='xl',
                                 color=c[color_principal]['200']),
                         height='100%',
                         width='40%',
                         bg=c[color_principal]['900'],
                         )
    else:
        item = rx.link(rx.center(rx.text(name,
                                         font_size='xl',
                                         _hover={'text-decoration': 'none'}),
                                 height='100%',
                                 bg=c[color_principal]['200'],
                                 width='100%',
                                 justify_content='center',
                                 boxShadow="5px 5px 10px rgba(0, 0, 0, 0.2)",
                                 border_radius=4,
                                 transition='background-color 0.3s',
                                 _hover={'background-color': c[color_principal]['100'],
                                         }
                             ),
                       href=href,
                       width='30%',
                       )
    return item


def navbar2(current_page):
    if current_page == 'aboutpage':
        barra = [
            breadcrumb_item('Pagina principal', href='/aboutpage', current=True),
            breadcrumb_item('Proyectos', href='/projects', current=False),
            breadcrumb_item('Experiencia', href='/experience', current=False)]
    elif current_page == 'projects':
        barra = [
            breadcrumb_item('Pagina principal', href='/aboutpage', current=False),
            breadcrumb_item('Proyectos', href='/projects', current=True),
            breadcrumb_item('Experiencia', href='/experience', current=False)]
    elif current_page == 'experience':
        barra = [
            breadcrumb_item('Pagina principal', href='/aboutpage', current=False),
            breadcrumb_item('Proyectos', href='/projects', current=False),
            breadcrumb_item('Experiencia', href='/experience', current=True)]
    else:
        barra = []

    return rx.breadcrumb(
        *barra,
        # separator='',
        display='stack',
        justify_content='center',
        width='95%',
        # boxShadow="5px 5px 10px rgba(0, 0, 0, 0.2)",
        # position="sticky", # Esta propiedad hace que la barra quede pegada arriba
        z_index="999",
        top="0"
    )