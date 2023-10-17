import reflex as rx

from portfolio_web.components.navbar import navbar2
from portfolio_web.styles import styles
from portfolio_web.views.experience.slider_structure import page
from portfolio_web.views.experience.footer import footer

header = rx.flex(rx.heading('Experiencia Laboral'),
                 align='center',
                 justify='center',
                 margin='10px')

def exp_page():
    return rx.vstack(
        navbar2('experience'),
        header,
        page,
        footer(),
        min_width='100%',
        height='100%',
        bg='#224040',
        margin=0,
        padding=0
    )

