import requests


def test_verify_api():
    url = "http://0.0.0.0:8000/verify?id=42&hash=abc123&taille=95"  # à adapter si ton serveur tourne sur une autre URL/port

    response = requests.get(url)

    print(f"Statut HTTP : {response.status_code}")
    print("Réponse JSON : ", response.json())


if __name__ == "__main__":
    test_verify_api()
