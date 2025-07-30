import requests


def test_verify_api():
    url = "http://192.168.1.47:8000/verify"  # à adapter si ton serveur tourne sur une autre URL/port

    # Exemple de paramètres de test
    params = {
        "id": 1,
        "hash": "helly",
        "taille": 1
    }

    response = requests.get(url, params=params)

    print(f"Statut HTTP : {response.status_code}")
    print("Réponse JSON : ", response.json())


if __name__ == "__main__":
    test_verify_api()
