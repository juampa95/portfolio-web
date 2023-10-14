import reflex as rx

from portfolio_web.components.navbar import navbar2
from portfolio_web.styles import styles
from portfolio_web.views.experience.slider import page

header = rx.flex(rx.heading('Experiencia Laboral'),
                 align='center',
                 justify='center',
                 margin='10px')

def exp_page():
    return rx.container(
        navbar2('experience'),
        header,
        page,
        min_width='100%',
        bg='#224040',
        margin=0,
        padding=0
    )

