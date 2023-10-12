import reflex as rx

from portfolio_web.components.navbar import navbar
from portfolio_web.styles import styles
from portfolio_web.views.projects_grid.project_cards_grid import get_repo_card

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
    )
    return rx.container(
        navbar(),
        rx.divider(),
        rx.heading('Proyectos en GitHub',
                   margin='1rem',
                   color='#BAD9D6'),
        project_grid,
        min_width='100%',
        bg='#224040'
    )

