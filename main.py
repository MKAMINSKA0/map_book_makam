users: list[dict[str, str]] = [
    {'name': 'Stas', 'surname': 'Grzymski', 'post': '1'},
    {'name': 'Kacper', 'surname': 'Macioch', 'post': '2'},
    {'name': 'Michał', 'surname': 'Krzywiński', 'post': '3'},
    {'name': 'Tymon', 'surname': 'Leszczyc', 'post': '2'},
    {'name': 'Michał', 'surname': 'Lębryk', 'post': '2'},
]
print(f'Witaj {users[0]["name"]}')

def read(users: list[dict[str, str]])->None:
    for user in users[1:]:
        print(f'Twój znajomy {user["name"]} opublikował  {user["post"]} posty')

read(users)

