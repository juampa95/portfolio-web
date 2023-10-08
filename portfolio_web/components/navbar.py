import reflex as rx


def navbar():
    return rx.flex(
        rx.box(
            rx.link(
                rx.image(src='/portafolio.png',width='50px',),
                href='/'
            )
        ),
        rx.center(
            rx.menu(
                rx.menu_button('MENU'),
                rx.menu_list(
                    rx.menu_item(
                        rx.link('About',
                                href='/aboutpage')
                    ),
                    rx.menu_item(
                        rx.link('Experience',
                                href='/experience'),
                    ),
                    rx.menu_item(
                        rx.link('Projects',
                                href='/projects'),
                    )
                )
            )
        ),
        justify_content='space-between',
        min_width='90%'
    )