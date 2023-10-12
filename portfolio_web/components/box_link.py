import reflex as rx


def box_link(text:str, url:str):
    return rx.link(rx.center(rx.heading(text,
                                           transition='font-size 0.3s',
                                           _hover={'font-size':'3em'}),
                                height='100%',
                             ),
                      href=url,
                      width='50%',
                      opacity='0.5',
                      transition='background-color 0.3s',
                      _hover={'opacity': 1,
                              'background-color':'#BAD9D6'
                              }
                      )