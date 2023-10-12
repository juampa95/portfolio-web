import reflex as rx


def navbar():
    return rx.flex(
        rx.box(
            rx.link(
                rx.image(src='/portafolio.png',width='50px',),
                href='/aboutpage'
            )
        ),
        rx.center(
            rx.menu(
                rx.menu_button('MENU',
                               as_='b'),
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
            )
        ),
        justify_content='space-between',
        min_width='90%'
    )

def navbar2():
    return