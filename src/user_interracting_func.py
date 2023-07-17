from src.api_class import HeadHunter, SuperJob
from src.add_vacancies_class import JsonSaverVacancy
from src.vacancies_class import Vacancy

#ЗП от. ЗП до, средняя ЗП. валюта, Опыт. сравнение зп средней
def get_HH_vacancies(search):

    hh = HeadHunter()
    hh_data = hh.get_vacancy(search)

    return hh_data

def get_SJ_vacancies(search):

    sj = SuperJob()
    sj_data = sj.get_vacancy(search)

    return sj_data

def search_vacancies(search, platform):
    vacancies_data = []

    if platform == 1:
        vacancies_data = get_HH_vacancies(search)
    elif platform == 2:
        vacancies_data = get_SJ_vacancies(search)
    elif platform == 3:
        vacancies_data = get_HH_vacancies(search) + get_SJ_vacancies(search)

    vacancies = []

    for item in vacancies_data:
        vacancy = Vacancy(item)
        vacancies.append(vacancy.create_dict())
    return vacancies

def save_to_json(search, platform):

    saved_data = JsonSaverVacancy()

    return saved_data.add_vacancy_to_file(search_vacancies(search, platform))

