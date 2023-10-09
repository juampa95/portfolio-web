import requests
import json


def get_information(username):
    url = f'https://api.github.com/users/{username}/repos'
    try:
        res = requests.get(url)
        res.raise_for_status()  # Genera una excepción si la solicitud falla (código de respuesta >= 400)
        data = res.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud a la API de GitHub: {e}")
        return None


def save_to_json(data, filename):
    with open(f'portfolio_web/utilitys/{filename}', 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    username = 'juampa95'
    repo_data = get_information(username)

    if repo_data is not None:
        filename = 'repos.json'
        save_to_json(repo_data, filename)
        print(f"La información de tus repositorios ha sido guardada en {filename}.")
    else:
        print("No se pudo obtener la información de los repositorios debido a un error en la solicitud.")
