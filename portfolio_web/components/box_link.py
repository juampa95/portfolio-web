import reflex as rx
from portfolio_web.styles.colors import colors as c
color_principal = 'spectra'


def box_link(text:str, url:str):
    return rx.link(rx.center(rx.heading(text,
                                        transition='font-size 0.3s',
                                        _hover={'font-size':'3em'}),
                             height='100%',
                             ),
                      href=url,
                      width='50%',
                      opacity='0.5',
                      transition='opacity 0.3s',
                      _hover={'opacity': 1,
                              'background-color': c[color_principal]['200']
                              }
                      )