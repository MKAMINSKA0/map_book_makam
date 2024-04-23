def read(users: list[dict[str, str]])->None:
    for user in users[1:]:
        print(f'Twój znajomy {user["name"]} opublikował  {user["post"]} posty')

    def add_user(Lista: list) -> None:
        user_name = input("Podaj imię: ")
        user_surname = input("Podaj nazwisko: ")
        user_post = input("Podaj ilosc postów: ")
        lista.append({'name': user_name, 'surname': user_surname, 'post': user_post})

