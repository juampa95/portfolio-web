import reflex as rx

boton_contacto = rx.menu(
    rx.menu_button('Contacto', bg='#BAD9D6', size='sm',
                   class_name='chakra-button css-yf5v12'), # para dar el mimso estilo, lo copie
                                                           # desde la consola de google crhome.
    rx.menu_list(
        rx.menu_item(rx.link('LinkedIn',
                             href='https://www.linkedin.com/in/juanpablomanzano/',
                             is_external=True)),
        rx.menu_divider(),
        rx.menu_item(rx.link('Email',
                             href='mailto:jpmanzano95@gmail.com',
                             is_external=True)),
        rx.menu_item(rx.link('WhatsApp',
                             href='https://api.whatsapp.com/send?phone=5492604395075',
                             is_external=True))
    ),
)