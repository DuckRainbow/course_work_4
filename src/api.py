from abc import ABC, abstractmethod

import requests


class APIData(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class GetVacancies(APIData):
    def __init__(self, page_num):
        self.__url_get = f'http://api.hh.ru/vacancies?per_page=100&page={page_num}'

    def get_vacancies(self):
        response = requests.get(self.__url_get)
        return response.text
