from src.api_class import HeadHunter, SuperJob
from src.add_vacancies_class import JsonSaverVacancy

#ЗП от. ЗП до, средняя ЗП. валюта, Опыт. сравнение зп средней
def get_HH_vacancies(search):

    hh = HeadHunter()
    hh_data = hh.get_vacancy(search)

    return hh_data

def get_SJ_vacancies(search):

    sj = SuperJob()
    sj_data = sj.get_vacancy(search)

    return sj_data
