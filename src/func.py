import requests


def get_vacancies():
    list_of_vacancies = []
    for page_num in range(20):
        url_get = f'http://api.hh.ru/vacancies?per_page=100&page={page_num}'
        responce = requests.get(url_get)
        list_of_vacancies.append(responce.text)
    return list_of_vacancies


if __name__ == '__main__':
    for vacancy in get_vacancies():
        print(vacancy)
        print(f'\n\n')
