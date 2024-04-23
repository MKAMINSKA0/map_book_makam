def read(users: list[dict[str, str]]) -> None:
    for user in users[1:]:
        print(f'twój znajomy {user["name"]} opublikował {user["post"]} posty ')


def add_user(lista: list) -> None:
    user_name = input('Podaj imie: ')
    user_surname = input('podaj nazwisko: ')
    user_post = input('podaj ile postów: ')
    lista.append({'name': user_name, 'surname': user_surname, 'post': user_post})

    def search(users: list[dict[str, str]]) -> None:
        user_name = input('Kogo szukasz? ')
        for user in users[1:]:
            if user['name'] == user_name:
                print(f'Znaleziono użytkownika {user}  ')


def remove_user(users: list[dict[str, str]]) -> None:
    user_name = input('Kogo usunąć? ')
    for user in users[1:]:
        if user['name'] == user_name:
            print(f'Znaleziono użytkownika {user['name']}  ')
            users.remove(user)
