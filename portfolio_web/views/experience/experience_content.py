import reflex as rx
from portfolio_web.views.experience.footer import card_footer
from portfolio_web.styles.colors import colors as c
color_principal = 'spectra'


with open('portfolio_web/views/experience/2015exp.md', 'r') as data:
    info2015 = data.read()

with open('portfolio_web/views/experience/2021exp.md', 'r') as data:
    info2021 = data.read()

with open('portfolio_web/views/experience/2022exp.md', 'r') as data:
    info2022 = data.read()


hard2015 = ['Excel','Word','Contabilidad','Matematicas', 'Tango gestion']
soft2015 = ['Responsabilidad','Atencion al publico','Comunicacion efectiva', 'Marketing', 'e-commerce']

exp2015 = rx.card(
    rx.markdown(info2015),
    header=rx.text('Administrativo contable semi-senior. [2015-2021]',
                   font_size='2xl',
                   as_='b',
                   color=c[color_principal]['800']
                   ),
    footer=card_footer(hard2015, soft2015),
    width='95%',
    bg=c[color_principal]['200'],
    marginBottom='0',
    boxShadow="10px 10px 20px rgba(0, 0, 0, 0.2)",

)

hard2021 = ['Excel','Word', 'Tango Gestion', 'Matematicas financieras', 'Contabilidad']
soft2021 = ['Trato con proveedores', 'Manejo de Caja', 'Responsabilidad', 'Pagos', 'Cheques y bancos',
            'Marketing', 'e-commerce']

exp2021 = rx.card(
    rx.markdown(info2021),
    header=rx.text('Encargado de pagos & administrativo junior [2021-2022]',
                   font_size='2xl',
                   as_='b',
                   color=c[color_principal]['800']
                   ),
    footer=card_footer(hard2021, soft2021),
    width='95%',
    bg=c[color_principal]['200'],
    marginBottom='0',
    boxShadow="10px 10px 20px rgba(0, 0, 0, 0.2)",

)

hard2022 = ['Excel','Word','SQL','Matematicas','Python', 'Logica', 'Resolucion de problemas']
soft2022 = ['Trabajo en Equipo', 'Lider', 'Responsabilidad','Manejo de personal','Planificacion', 'Oratoria',
            'Pensamiento critico', 'Toma de decisiones']

exp2022 = rx.card(
    rx.markdown(info2022),
    header=rx.text('Ingeniero industrial junior - oficina técnica [2022-Actualidad]',
                   font_size='2xl',
                   as_='b',
                   color=c[color_principal]['800']
                   ),
    footer=card_footer(hard2022, soft2022),
    width='95%',
    bg=c[color_principal]['200'],
    marginBottom='0',
    boxShadow="10px 10px 20px rgba(0, 0, 0, 0.2)",

)