import reflex as rx

from portfolio_web.components.navbar import navbar2
from portfolio_web.base_state import State
from portfolio_web.styles import styles
from portfolio_web.views.experience.experience_content import exp2015, exp2021, exp2022
from portfolio_web.styles.colors import colors as c
color_principal = 'spectra'


class SliderState(State):
    value: int = 2023


def slider():
    return rx.hstack(
        rx.vstack(
            rx.heading(SliderState.value,
                       size='md',
                       margin_bottom='10px'),
            rx.slider(rx.slider_track(
                    rx.slider_filled_track(bg=c[color_principal]['200']),
                    bg=c[color_principal]['700'],
                ),
                rx.slider_thumb(
                    box_size='1.5em',
                    bg=c[color_principal]['200']),
                # rx.slider_mark(), # No tengo como posicionarlos
                on_change=SliderState.set_value,
                orientation='vertical',
                min_h='500px',
                default_value=2023,
                min_=2015,
                max_=2023,
                      ),
            width='50px',
        ),
        rx.vstack(
            rx.flex(rx.text('INGENIERO INDUSTRIAL',
                            as_='b',
                            font_size='xs',
                            transform='rotate(270deg)'),
                    height='19%',
                    align='center'),
            rx.divider(),
            rx.flex(rx.text('ENCARGADO',
                            as_='b',
                            font_size='xs',
                            transform='rotate(270deg)'
                            ),
                    height='19%',
                    align='center'),
            rx.divider(),
            rx.flex(rx.text('ADMINISTRATIVO CONTABLE',
                            as_='b',
                            font_size='xs',
                            transform={'rotate(270deg)'},
                            ),
                    height='62%',
                    align='center'),
            height='500px',
            width='50px',

        ),
        spacing='0'
    )

def body():
    condicional = rx.cond(
        SliderState.value > 2021,
        exp2022,
        rx.cond(
            SliderState.value < 2021,
            exp2015,
            exp2021))
    return condicional


page = rx.hstack(
    slider(),
    body(),
    width='100%'
)