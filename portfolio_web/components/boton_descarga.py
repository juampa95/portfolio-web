import reflex as rx
from portfolio_web.base_state import State


class ModalState(State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


boton_descarga = rx.box(
    rx.button('Descargar CV', bg='#BAD9D6', size='sm',
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
                        bg='#D9BABA', size='sm'
                    ),
                    rx.link(rx.button('Descargar',
                                      bg='#BAD9D6',
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