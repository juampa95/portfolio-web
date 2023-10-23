import reflex as rx
from portfolio_web.styles.colors import colors as c

color_principal = 'spectra'

boton_contacto = rx.menu(
    rx.menu_button('Contacto', bg=c[color_principal]['200'], size='sm',
                   class_name='chakra-button css-1ykrb1k'),  # para dar el mimso estilo, lo copie
    # desde la consola de google crhome.
    rx.menu_list(
        rx.link(rx.menu_item('LinkedIn'),
                href='https://www.linkedin.com/in/juanpablomanzano/',
                is_external=True),
        rx.menu_divider(),
        rx.link(rx.menu_item('Email'),
                href='mailto:jpmanzano95@gmail.com',
                is_external=True),
        rx.link(rx.menu_item('WhatsApp'),
                href='https://api.whatsapp.com/send?phone=5492604395075',
                is_external=True)
    ),
)
