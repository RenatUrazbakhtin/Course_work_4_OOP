from abc import ABC, abstractmethod
from src.vacancies_class import Vacancy

class JsonSaver(ABC):
    @abstractmethod
    def add_vacancy_to_file(self, vacancy):
        pass
    @abstractmethod
    def get_vacancy_by_salary(self, search):
        pass

    @abstractmethod
    def get_vacancy_by_experience(self, search):
        pass

    @abstractmethod
    def get_vacancy_by_currency(self, search):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

class JsonSaverVacancy(JsonSaver):
    def add_vacancy_to_file(self, vacancy):
        pass

    def get_vacancy_by_salary(self, search):
        pass

    def get_vacancy_by_experience(self, search):
        pass

    def get_vacancy_by_currency(self, search):
        pass

    def delete_vacancy(self, vacancy):
        pass

#запись в файл
#достаем
#чистка