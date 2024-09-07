import requests
def jokes() -> str:
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
    data = response.json()
    status = response.status_code
    if status==200:
        category = data.get("category")
        jokewords = data.get("joke")
        joke = f"category: {category}\njoke: {jokewords}"

        return joke