# Импортирование нужных модулей и пакетов
from abc import ABC, abstractmethod
from src.vacancies_class import Vacancy
from src.api_class import HeadHunter, SuperJob
import json

class JsonSaver(ABC):
    """
    Абстрактный класс для сохранения вакансий в файл search.json и фильтрации вакансий
    """
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
    def delete_vacancy(self):
        pass

class JsonSaverVacancy(JsonSaver):
    def add_vacancy_to_file(self, vacancy: list, filename="search.json"):
        """
        Сохраняет вакансии в файл search.json
        :param vacancy: список вакансий
        :param filename: название файла
        :return: сохраняет данные в файл
        """
        with open(filename, "w") as file:
            json.dump(vacancy, file, indent=2, ensure_ascii=False)


    def get_vacancy_by_salary_average(self, search, vacancy: list):
        """
        фильтрация вакансии по уровню средней ЗП
        :param search: поисковый запрос пользователя
        :param vacancy: список вакансий
        :return: отфильтрованный список вакансий
        """
        vacancy_list_by_salary = []
        for item in vacancy:
            if item["ЗП"]["Средняя ЗП"] == int(search):
                vacancy_list_by_salary.append(item)
            elif type(item["ЗП"]["Средняя ЗП"]) == str:
                continue
        return vacancy_list_by_salary

    def get_vacancy_by_salary_from(self, search, vacancy):
        """
        Фильтрация вакансий по ЗП от
        :param search: поисковый запрос пользователя
        :param vacancy: список вакансий
        :return: отфильтрованный список вакансий
        """
        vacancy_list_by_salary = []
        for item in vacancy:
            if type(item["ЗП"]["От"]) == str:
                continue
            elif item["ЗП"]["От"] >= int(search):
                vacancy_list_by_salary.append(item)
        return vacancy_list_by_salary

    def get_vacancy_by_salary_to(self, search, vacancy):
        """
        Фильтрация по уровню ЗП до
        :param search: поисковый запрос пользователя
        :param vacancy: список вакансий
        :return: отфильтрованный список вакансий
        """
        vacancy_list_by_salary = []
        for item in vacancy:
            if type(item["ЗП"]["До"]) == str:
                continue
            elif item["ЗП"]["До"] <= int(search):
                vacancy_list_by_salary.append(item)
        return vacancy_list_by_salary

    def get_vacancy_by_experience(self, search, vacancy):
        """
        Фильтрация по опыту работы
        :param search: поисковый запрос пользователя
        :param vacancy: список вакансий
        :return: отфильтрованный список вакансий
        """
        vacancy_list_by_experience = []
        for item in vacancy:
            if item["Опыт работы"].lower() == search:
                vacancy_list_by_experience.append(item)
        return vacancy_list_by_experience


    def get_vacancy_by_currency(self, search, vacancy):
        """
        Фильтрация по валюте
        :param search: поисковый запрос пользователя
        :param vacancy: список вакансий
        :return: отфильтрованный список
        """
        vacancy_list_by_currency = []
        for item in vacancy:
            if item["ЗП"]["Валюта"] == str(search):
                vacancy_list_by_currency.append(item)
        return vacancy_list_by_currency

    def delete_vacancy(self):
       with open('search.json', "wt") as file:
        file.write("")

    def delete_search_vacancies(self, search):
        with open('search.json') as file:
            dicts = json.load(file)
            new_dict = []
            for item in dicts:
                if search.capitalize() in item.values():
                    pass
                else:
                    new_dict.append(item)

        with open('search.json', 'w') as file:
            json.dump(new_dict, file, indent=2, ensure_ascii=False)



