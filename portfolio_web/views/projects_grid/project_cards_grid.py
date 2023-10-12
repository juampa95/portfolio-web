import reflex as rx
import json

from portfolio_web.base_state import State

class RepoInfo(State):
    """Clase que obtiene los parametros deseados de los repositorios
    que se encuentran en el archivo repos.json obtenido desde la
    API de GitHub con el script repos_github.py en el dir utilitys"""
    description = ''
    created_at = ''
    updated_at = ''
    language = ''
    topics = []
    url = ''
    homepage = ''

    def get_info(self, repo_name):
        """Al pasarle el nombre del repositorio, obtiene los parametros solo para este"""
        with open('portfolio_web/utilitys/repos.json', 'r') as json_file:
            data = json.load(json_file)
        for i in range(len(data)):
            if data[i]['name'] == repo_name:
                self.description = data[i]['description']
                self.created_at = data[i]['created_at']
                self.updated_at = data[i]['updated_at']
                self.language = data[i]['language']
                self.topics = data[i]['topics']
                self.url = data[i]['html_url']
                self.homepage = data[i]['homepage']

def get_repo_card(repo_name):
    """Esta funcion se encarga de armar las card de cada proyecto, y las une en una responsive_grid
    dentro del objeto topics.
    Para armar las cards, usa el objeto RepoInfo y la funcion que obtiene la informacion de los mismos
    get_info para cada repositorio. Devuelve toda la informacion, pero solo uso la descripcion,
    fecha de creacion y actualizacion, y los tags que tenga el repositorio. """
    repo_info = RepoInfo()
    repo_info.get_info(repo_name)
    # creado = datetime.strptime(repo_info.created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
    # ultima_actualizacion = datetime.strptime(repo_info.updated_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
    creado = repo_info.created_at[:10]  # Extrae la parte de la fecha (YYYY-MM-DD)
    ultima_actualizacion = repo_info.updated_at[:10]  # Extrae la parte de la fecha (YYYY-MM-DD)
    tags = repo_info.topics
    desplegada = repo_info.homepage

    # tags es una lista que puede contener o no tags. Entonces planteamos lo siguiente
    # si no tiene tags, ponemos fecha de creacion y ultima actualizacion. Si tiene tags
    # hacemos una lista de componentes rx.tag para cada uno y luego la desempaqueta en el
    # componente responsive grid.

    if not tags:
        topics = rx.responsive_grid(
            rx.box(
                rx.text('creado:'),
                rx.tag(creado),
            ),
            rx.box(
                rx.text('actualizdo:'),
                rx.tag(ultima_actualizacion),
            ),
            columns=[1,2],
            spacing='3',
            marging_top='1rem'
        )
    else:
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
            gap='2'
        )
    if desplegada != '':
        boton_despliegue = rx.link(rx.button('Deployed',
                                             bg='#4D8C63',
                                             boxShadow="5px 5px 10px rgba(0, 0, 0, 0.2)",
                                             color_scheme='blackAlpha'
                                             ),
                                   href=desplegada
                                   )

    else:
        boton_despliegue = rx.box('')

    # Por ultimo, la funcion get_repo_card devuelve la card de cada repositorio, que contiene
    # un componente box con la descripcion del proyecto y una responsive_grid con los topcis
    # que pueden ser una lista de tags, o la fecha de creacion y actualizacion. Tambien cada
    # card tiene un titulo y un footer con el link al repositorio en cuestion.

    return rx.card(
        rx.box(
            rx.text(repo_info.description,
                    size="sm"),
            topics,
            width='100%'
        ),
        header=rx.flex(
            rx.heading(repo_name,
                          size='md',
                          as_='b',
                          color='#224040'),
            boton_despliegue,
            justify='space-between'),
        footer=rx.grid(rx.link(rx.button('GitHub',
                                         boxShadow="5px 5px 10px rgba(0, 0, 0, 0.2)",
                                         color_scheme='blackAlpha',
                                         # bg='#BAD9D6',
                                         ),
                                 href=repo_info.url),
                       rx.responsive_grid(
                          rx.box(
                              rx.text('creado:',
                                      size='xs'),
                              rx.tag(creado),
                          ),
                          rx.box(
                              rx.text('actualizdo:',
                                      size='xs'),
                              rx.tag(ultima_actualizacion),
                          ),
                          columns=[1, 2],
                          spacing='3',
                          marging_top='1rem'
                      ),
                       template_columns='1fr 2fr',
                       gap='10',
                       alignItems='flex-end'
                      ),
        bg='#BAD9D6',
        marginBottom='0',
        boxShadow="10px 10px 20px rgba(0, 0, 0, 0.2)",
        opacity=0.8,
        transition= 'background-color 0.3s, box-shadow 0.3s, opacity 0.3s',
        _hover={'opacity':1,
                'background-color':'#BAD9D6',
                'box-shadow': '0 0 20px rgba(0, 0, 0, 0.5)'}
    )
