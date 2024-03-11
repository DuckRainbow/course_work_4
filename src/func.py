def filter_city(vacancies_list, city):
    if city.lower() != 'нет':
        new_list = []
        for vacancy in vacancies_list:
            if vacancy.city == city:
                new_list.append(vacancy)
        return new_list
    return vacancies_list


def filter_vacancies(city_vacancies, filter_words):
    if filter_words.lower() != 'нет':
        words = filter_words.split(' ')
        new_list = []
        for vacancy in city_vacancies:
            for word in words:
                if words in vacancy.description or words in vacancy.requirements:
                    new_list.append(vacancy)
        return new_list
    return city_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    if salary_range.lower() != 'нет':
        salary = salary_range.split(' ')
        new_list = []
        for vacancy in filtered_vacancies:
            if int(salary[0]) <= vacancy.salary_from <= int(salary[1]):
                if vacancy not in new_list:
                    new_list.append(vacancy)
            elif int(salary[0]) <= vacancy.salary_to <= int(salary[1]):
                if vacancy not in new_list:
                    new_list.append(vacancy)
        return new_list
    return filtered_vacancies


def sort_vacancies(ranged_vacancies):
    sorted_vacancies = sorted(ranged_vacancies)
    return sorted_vacancies


def get_top_vacancies(sorted_vacancies, top_n):
    new_list = sorted_vacancies[:top_n]
    return new_list


def print_vacancies(top_vacancies):
    for vacancy in top_vacancies:
        print(vacancy)
