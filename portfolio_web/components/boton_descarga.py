import reflex as rx
from portfolio_web.base_state import State
from portfolio_web.styles.colors import colors as c
color_principal = 'spectra'
color_secundario = 'cavern-pink'


class ModalState(State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


boton_descarga = rx.box(
    rx.button('Descargar CV', bg=c[color_principal]['200'], size='sm',
              on_click=ModalState.change),
    rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header("Confirmacion"),
                rx.modal_body(
                    'Desea descargar el CV en formato PDF?'
                ),
                rx.modal_footer(
                    rx.button(
                        'Cancelar', on_click=ModalState.change,
                        bg=c[color_secundario]['300'], size='sm'
                    ),
                    rx.link(rx.button('Descargar',
                                      bg=c[color_principal]['200'],
                                      size='sm',
                                      on_click=ModalState.change,
                                      ),
                            href='/CV_IT_1.pdf',
                            is_external=True,
                    ),
                    direction='row',
                    justify='left',
                    margin_top='1em',
                    gap=3,
                ),
            )
        ),
        is_open=ModalState.show,
    ),
)