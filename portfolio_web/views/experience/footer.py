import reflex as rx



def footer():
    r = rx.link(rx.center(rx.heading('Descargar CV',
                                     transition='font-size 0.3s',
                                     _hover={'font-size': '3em'}),
                          ),
                href='/CV_IT_1.pdf',
                width='100%',
                opacity='0.5',
                bg='#224040',
                is_external=True,
                transition='opacity 0.3s',
                _hover={'opacity': 1,
                        'background-color': '#BAD9D6'
                        }
                )

    return r


def tags_grid(tags):
    tag_components = []
    for tag in tags:
        tag_components.append(
            rx.tag(tag,
                   bg='#345959',
                   color='#BAD9D6'),
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
        align_items='left'
    )