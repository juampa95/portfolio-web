"""The main Reflex website."""

import reflex as rx
import requests
import random


from portfolio_web.components.header import header
from portfolio_web.components.navbar import navbar
from portfolio_web.pages.experiencia import exp_page
from portfolio_web.pages.projects import projects_page
from portfolio_web.styles import styles
from portfolio_web.base_state import State


def index():
    return rx.container(
        navbar(),
        rx.divider(),
        header(),
        min_width='100%'
    )


def about():
    return rx.container(
        navbar(),
        rx.divider(),
        min_width='100%'
    )


app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
)

app.add_page(index)
app.add_page(about, route='/aboutpage')
app.add_page(exp_page, route='/experience')
app.add_page(projects_page, route='/projects')
app.compile()
