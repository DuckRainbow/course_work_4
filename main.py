# Функция для взаимодействия с пользователем
from src.func import filter_city, filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, \
    print_vacancies


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    print('Следующие параметры опциональны, если вам не нужен какой-либо фильтр, напишите "нет" в ответе.\n')
    city = input('Введите название города')
    filter_words = input("Введите ключевые слова для фильтрации вакансий(через пробел): ").split(' ')
    salary_range = input("Введите диапазон зарплат(через пробел): ")  # Пример: 100000 - 150000



    city_vacancies = filter_city(vacancies_list, city)

    filtered_vacancies = filter_vacancies(city_vacancies, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
