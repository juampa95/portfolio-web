import reflex as rx

from portfolio_web.components.navbar import navbar2
from portfolio_web.styles import styles
from portfolio_web.views.experience.slider_structure import page
from portfolio_web.views.experience.footer import footer

from portfolio_web.styles.colors import colors as c
color_principal = 'spectra'

header = rx.flex(rx.heading('Experiencia Laboral'),
                 align='center',
                 justify='center',
                 margin='10px',
                 color=c[color_principal]['200'])

def exp_page():
    return rx.vstack(
        navbar2('experience'),
        header,
        page,
        footer(),
        min_width='100%',
        height='100vh',
        bg=c[color_principal]['900'],
        margin=0,
        padding=0,
        padding_bottom=2
    )

