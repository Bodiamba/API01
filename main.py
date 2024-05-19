import requests

# Запрос идентификатора покемона у пользователя
pokemon_id = input("Введите идентификатор покемона: ")

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Name:", data["name"])
    print("Height:", data["height"])
    print("Weight:", data["weight"])
    print("Abilities:")
    for ability in data["abilities"]:
        print("-", ability["ability"]["name"])
else:
    print("Ошибка при получении данных. Пожалуйста, убедитесь, что введен корректный идентификатор покемона.")