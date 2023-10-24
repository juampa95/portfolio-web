import reflex as rx
from portfolio_web.styles.colors import colors as c
color_principal = 'spectra'


def footer():
    r = rx.link(rx.center(rx.heading('Descargar CV',
                                     size='lg',
                                     transition='font-size 0.3s',
                                     _hover={'font-size': '2.2em'}),
                          ),
                href='/CV_IT_1.pdf',
                width='100%',
                # height='100%',
                opacity='0.5',
                bg=c[color_principal]['900'],
                is_external=True,
                transition='opacity 0.3s',
                _hover={'opacity': 1,
                        'background-color': c[color_principal]['200']
                        }
                )

    return r


def tags_grid(tags):
    tag_components = []
    for tag in tags:
        tag_components.append(
            rx.tag(tag,
                   bg=c[color_principal]['800'],
                   color=c[color_principal]['200']),
        )
    topics = rx.flex(
        *tag_components,
        margin_top='1rem',
        wrap='wrap',
        gap='2',
    )
    return topics


def card_footer(hard,soft):
    return rx.vstack(
        rx.text('Hard Skills Utilizados',
                as_='b'),
        tags_grid(hard),
        rx.text('Soft Skills Utilizados',
                as_='b'),
        tags_grid(soft),
        align_items='left',
        margin=0,
        padding=0
    )