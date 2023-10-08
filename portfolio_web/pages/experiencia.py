import reflex as rx

from portfolio_web.components.navbar import navbar
from portfolio_web.styles import styles


def exp_page():
    return rx.container(
        navbar(),
        rx.divider(),
        rx.text('hola como estas'),
        min_width='95%'
    )

