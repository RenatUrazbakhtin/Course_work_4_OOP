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
            elif item["ЗП"]["До"] == int(search):
                vacancy_list_by_salary.append(item)
        return vacancy_list_by_salary

    def get_vacancy_by_experience(self, search, vacancy):
        vacancy_list_by_experience = []
        for item in vacancy:
            if item["Опыт работы"] == search:
                vacancy_list_by_experience.append(item)
        return vacancy_list_by_experience


    def get_vacancy_by_currency(self, search, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass

# def hh_exmpl():
#     hh = HeadHunter()
#     get_vacancy = hh.get_vacancy("Менеджер")
#     return get_vacancy
#
# def norm_vid():
#     new_list = []
#     for item in hh_exmpl():
#         vacancy = Vacancy(item)
#         new_list.append(vacancy.create_dict())
#     return new_list
#
# def json_asd():
#     a = JsonSaverVacancy()
#     a.add_vacancy_to_file(norm_vid())
#     return a
# def json_exmpl():
#     a = JsonSaverVacancy()
#     return a.get_vacancy_by_salary_average(20000, norm_vid())
#
# def salary_from():
#     a = JsonSaverVacancy()
#     return a.get_vacancy_by_salary_from(20000, norm_vid())
#
# def salary_to():
#     a = JsonSaverVacancy()
#     return a.get_vacancy_by_salary_to(60000, norm_vid())
#
# def exp():
#     a = JsonSaverVacancy()
#     return a.get_vacancy_by_experience("Без опыта", norm_vid())
#
# print(exp())
# print(salary_to())
# print(json_exmpl())
# print(get_vacancy)
# new_list = []
# for item in get_vacancy:
#     vacancy = Vacancy(item)
#     new_list.append(vacancy.create_dict())


#запись в файл
#достаем
#чистка