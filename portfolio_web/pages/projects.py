import reflex as rx

from portfolio_web.components.navbar import navbar, navbar2
from portfolio_web.styles import styles
from portfolio_web.views.projects_grid.project_cards_grid import get_repo_card
from portfolio_web.styles.colors import colors as c

color_principal = 'spectra'

def barra_inf():
    return rx.stack(
        rx.link(
            rx.vstack(
                rx.text('VER TODOS LOS PROYECTOS',
                                    size='md',
                                    as_='b',
                                    color=c[color_principal]['200']
                                    ),
                rx.image(src='/github_icon.svg',
                         width='100px'),
                height='100%',
                justify_content='center'
                ),
            href='https://github.com/juampa95',
            is_external=True
        ),
        rx.image(src='https://github-readme-stats.vercel.app/api?username=juampa95&theme=dark&show_icons=true&locale=es',
                 width=['300px','300px','467px','467px','467px'],
                 display=['none','none','flex','flex','flex']),
        # rx.image(src='https://github-readme-stats.vercel.app/api/top-langs/?username=juampa95&theme=dark&show_icons=true&locale=es'),
        direction='row',
        align='center',
        justify_content='center',
        widht='100%',
        spacing='20px',
        padding_bottom='10px')


projects_name = ['portfolio-web',
                 'api-med',
                 'api_vercel',
                 'cnn-ocr',
                 'customer-churn-ds',
                 'ocr-project',
                 'scraping_licitaciones_gob',
                 'web_scraping',
                 'web-app'
                 ]

def projects_page():
    """Funcion encargada de distribuir la pagina de proyectos. Hacemos una lista de proyectos y le
    agregamos el elemento card creado por la funcion get_repo_card para cada proyecto en la lista
    projects_name. luego desempaquetamos esta lista de projects en una responsive grid para cada
    elemento de la lista projects. Luego devuelve un container con su navbar, heading y por ultimo
    la project_grid."""
    projects = []
    for p in projects_name:
        projects.append(
            get_repo_card(p)
        )
    project_grid = rx.responsive_grid(
        *projects,
        columns=[1, 2, 3, 4],
        min_child_width='380px',
        spacing='4',
        margin=5
    )
    return rx.vstack(
        navbar2('projects'),
        rx.heading('Proyectos en GitHub',
                   margin='1rem',
                   color=c[color_principal]['200']),
        project_grid,
        barra_inf(),
        min_width='100%',
        bg=c[color_principal]['900'],
        margin=0,
        padding_top=0,
        padding_left=3,
        padding_right=3,
    )

