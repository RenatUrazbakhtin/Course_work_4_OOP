from abc import ABC, abstractmethod
from src.vacancies_class import Vacancy
from src.api_class import HeadHunter, SuperJob
import json

class JsonSaver(ABC):
    @abstractmethod
    def add_vacancy_to_file(self, vacancy, filename="search.json"):
        pass
    @abstractmethod
    def get_vacancy_by_salary_average(self, search, vacancy):
        pass
    @abstractmethod
    def get_vacancy_by_salary_from(self, search, vacancy):
        pass
    @abstractmethod
    def get_vacancy_by_salary_to(self, search, vacancy):
        pass

    @abstractmethod
    def get_vacancy_by_experience(self, search, vacancy):
        pass

    @abstractmethod
    def get_vacancy_by_currency(self, search, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

class JsonSaverVacancy(JsonSaver):
    def add_vacancy_to_file(self, vacancy: list, filename="search.json"):
        with open(filename, "w") as file:
            json.dump(vacancy, file, indent=2, ensure_ascii=False)


    def get_vacancy_by_salary_average(self, search, vacancy: list):
        vacancy_list_by_salary = []
        for item in vacancy:
            if item["ЗП"]["Средняя ЗП"] == int(search):
                vacancy_list_by_salary.append(item)
            elif type(item["ЗП"]["Средняя ЗП"]) == str:
                continue
        return vacancy_list_by_salary

    def get_vacancy_by_salary_from(self, search, vacancy):
        vacancy_list_by_salary = []
        for item in vacancy:
            if type(item["ЗП"]["От"]) == str:
                continue
            elif item["ЗП"]["От"] >= int(search):
                vacancy_list_by_salary.append(item)
        return vacancy_list_by_salary

    def get_vacancy_by_salary_to(self, search, vacancy):
        vacancy_list_by_salary = []
        for item in vacancy:
            if type(item["ЗП"]["До"]) == str:
                continue
            elif item["ЗП"]["До"] <= int(search):
                vacancy_list_by_salary.append(item)
        return vacancy_list_by_salary

    def get_vacancy_by_experience(self, search, vacancy):
        vacancy_list_by_experience = []
        for item in vacancy:
            if item["Опыт работы"] == search:
                vacancy_list_by_experience.append(item)
        return vacancy_list_by_experience


    def get_vacancy_by_currency(self, search, vacancy):
        vacancy_list_by_currency = []
        for item in vacancy:
            if item["Валюта"] == search:
                vacancy_list_by_currency.append(item)
        return vacancy_list_by_currency

    def delete_vacancy(self, vacancy):
       pass


