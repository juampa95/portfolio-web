import reflex as rx


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

## El breadcrumb por defecto dio muchos errores.

# def breadcrumb_item(name: str, href :str, current :bool):
#     if current:
#         item = rx.breadcrumb_item(rx.breadcrumb_link(name,
#                                                      font_size='xl',
#                                                      color='#BAD9D6'),
#                                   is_current_page=True,
#                                   bg='#224040',
#                                   width='39%',
#                                   justify_content='center')
#     else:
#         item = rx.link(rx.breadcrumb_item(rx.breadcrumb_link(name, href=href,
#                                                              font_size='xl',
#                                                              _hover={'text-decoration':'none'}),
#                                           is_current_page=False,
#                                           bg='#BAD9D6',
#                                           width='100%',
#                                           justify_content='center',
#                                           opacity='0.5',
#                                           transition='opacity 0.3s',
#                                           _hover={'opacity': 1,
#                                                   }
#                                           ),
#                        href=href,
#                        width='30%')
#
#     return item
#
#
# def navbar2(current_page):
#     if current_page == 'aboutpage':
#         barra = [
#             breadcrumb_item('About', href='/aboutpage', current=True),
#             breadcrumb_item('Projects', href='/projects', current=False),
#             breadcrumb_item('Experience', href='/experience', current=False)]
#     elif current_page == 'projects':
#         barra = [
#             breadcrumb_item('About', href='/aboutpage', current=False),
#             breadcrumb_item('Projects', href='/projects', current=True),
#             breadcrumb_item('Experience', href='/experience', current=False)]
#     elif current_page == 'experience':
#         barra = [
#             breadcrumb_item('About', href='/aboutpage', current=False),
#             breadcrumb_item('Projects', href='/projects', current=False),
#             breadcrumb_item('Experience', href='/experience', current=True)]
#     else:
#         barra = []
#
#     return rx.breadcrumb(
#         *barra,
#         separator='',
#         display='stack',
#         justify_content='center',
#         width='100%',
#     )
#

def breadcrumb_item(name: str, href :str, current :bool):
    if current:
        item = rx.center(rx.text(name,
                                 font_size='xl',
                                 color='#BAD9D6'),
                         height='100%',
                         width='40%')
    else:
        item = rx.link(rx.center(rx.text(name,
                                         font_size='xl',
                                         _hover={'text-decoration': 'none'}),
                                 height='100%',
                                 bg='#BAD9D6',
                                 width='100%',
                                 justify_content='center',
                                 opacity='0.5',
                                 transition='opacity 0.3s',
                                 _hover={'opacity': 1,
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
        separator='',
        display='stack',
        justify_content='center',
        width='100%',
    )