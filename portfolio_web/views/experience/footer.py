import reflex as rx


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


def footer(hard,soft):
    return rx.vstack(
        rx.text('Hard Skills Utilizados',
                as_='b'),
        tags_grid(hard),
        rx.text('Soft Skills Utilizados',
                as_='b'),
        tags_grid(soft),
        align_items='left'
    )