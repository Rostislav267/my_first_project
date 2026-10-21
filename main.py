import requests

username = input("Введите username на GitHub: ")
response = requests.get(f"https://api.github.com/users/{username}")

if response.status_code == 200:
    data = response.json()
    print(f"Имя: {data['name']}")
    print(f"Репозиториев: {data['public_repos']}")
    print(f"Подписчиков: {data['followers']}")
else:
    print("Пользователь не найден")