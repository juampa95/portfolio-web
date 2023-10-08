import reflex as rx
import requests
import random
from portfolio_web.base_state import State


class MyState(State):
    quote = ''
    author = ''

    def get_quote(self):
        url = 'https://type.fit/api/quotes'
        res = requests.get(url)
        data = res.json()
        rand_num = random.randrange(0, len(data))
        self.quote = data[rand_num]['text']
        self.author = data[rand_num]['author']



def header():
    return rx.responsive_grid(
        rx.center(
            rx.box(
                rx.heading('Soy Juan Pablo!', size='xl'),
                rx.heading('Pyhton developer', size='sm'),
                rx.button('Click here', margin_top='2rem',
                          on_click=MyState.get_quote),
                quote()
            )
        ),
        rx.center(
            rx.image(src='/portafolio.png')
        ),
        columns=[1,2],
        min_width='95%'
    )


def quote():
    return rx.box(
        rx.text(MyState.quote, as_='b'),
        rx.text(MyState.author),
        margin_top='2rem'
    )