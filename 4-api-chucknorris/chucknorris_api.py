import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        joke = response.json()['value']  
        print("Piada do Chuck Norris:", joke)
    
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição: {e}")
    except ValueError:
        print("Erro ao tentar processar a resposta da API.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

get_chuck_norris_joke()
