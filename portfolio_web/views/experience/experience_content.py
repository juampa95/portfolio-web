import reflex as rx
from portfolio_web.views.experience.footer import footer

with open('portfolio_web/views/experience/2015exp.md', 'r') as data:
    info2015 = data.read()

with open('portfolio_web/views/experience/2021exp.md', 'r') as data:
    info2021 = data.read()

with open('portfolio_web/views/experience/2022exp.md', 'r') as data:
    info2022 = data.read()


hard2015 = ['Excel','Word','Contabilidad','Matematicas']
soft2015 = ['Responsabilidad','Atencion al publico','Comunicacion efectiva']

exp2015 = rx.card(
    rx.markdown(info2015),
    header=rx.text('Administrativo contable semi-senior. [2015-2021]',
                   font_size='2xl',
                   as_='b',
                   color='#224040'
                   ),
    footer=footer(hard2015, soft2015),
    width='85%',
    bg='#BAD9D6',
    marginBottom='0',
    boxShadow="10px 10px 20px rgba(0, 0, 0, 0.2)",

)

hard2021 = ['Excel','Word','SQL']
soft2021 = ['Trabajo en Equipo', 'Lider', 'Responsabilidad']

exp2021 = rx.card(
    rx.markdown(info2021),
    header=rx.text('Encargado de pagos & administrativo junior [2021-2022]',
                   font_size='2xl',
                   as_='b',
                   color='#224040'
                   ),
    footer=footer(hard2021, soft2021),
    width='85%',
    bg='#BAD9D6',
    marginBottom='0',
    boxShadow="10px 10px 20px rgba(0, 0, 0, 0.2)",

)

hard2022 = ['Excel','Word','SQL','Matematicas','Python']
soft2022 = ['Trabajo en Equipo', 'Lider', 'Responsabilidad','Manejo de personal','Planificacion']

exp2022 = rx.card(
    rx.markdown(info2022),
    header=rx.text('Ingeniero industrial junior - oficina técnica [2022-Actualidad]',
                   font_size='2xl',
                   as_='b',
                   color='#224040'
                   ),
    footer=footer(hard2022, soft2022),
    width='85%',
    bg='#BAD9D6',
    marginBottom='0',
    boxShadow="10px 10px 20px rgba(0, 0, 0, 0.2)",

)