import os
from abc import ABC, abstractmethod
import requests, json

class ApiKeys(ABC):
    @abstractmethod
    def get_vacancy(self, search):
       pass


class HeadHunter(ApiKeys):

    def __init__(self, url="https://api.hh.ru/vacancies"):
        self.url = url

    def get_vacancy(self, search):

        param = {"text": search, "page_from": 0, "page_to": 50}
        request = requests.get(self.url, params=param)
        data = request.json()["items"]

        vacancies = []

        for item in data:
            vacancy = {"name": item["name"], "url": item["alternate_url"], "employment": item["employment"]["name"], 'experience': item['experience']['name']}

            if item['experience']['name'] == 'Нет опыта':
                vacancy['experience'] = 'Без опыта'
            elif item['experience']['name'] == 'От 1 года до 3 лет':
                vacancy['experience'] = 'От 1 года'
            elif item['experience']['name'] == 'От 3 до 6 лет':
                vacancy['experience'] = 'От 3 лет'
            elif item['experience']['name'] == 'Более 6 лет':
                vacancy['experience'] = 'От 6 лет'
            else:
                vacancy["experience"] = "Значение не указано"

            if item['salary'] is None:
                vacancy['min_salary'] = 'По результатам собеседования'
                vacancy['max_salary'] = 'По результатам собеседования'
                vacancy['currency'] = 'Не указано'
            else:
                if item['salary']['from'] is None:
                    vacancy['min_salary'] = 'Минимальная зарплата не указана'
                else:
                    vacancy['min_salary'] = item['salary']['from']

                if item['salary']['to'] is None:
                    vacancy['max_salary'] = 'Максимальная зарплата не указана'
                else:
                    vacancy['max_salary'] = item['salary']['to']
                if item['salary']['currency'] == 'RUR':
                    vacancy['currency'] = 'RUB'
                else:
                    vacancy['currency'] = item['salary']['currency']

            vacancies.append(vacancy)

        return vacancies
class SuperJob(ApiKeys):
    def __init__(self, url='https://api.superjob.ru/2.0/vacancies/'):
        self.url = url

    def get_vacancy(self, search):

        sj_api_key: str = os.getenv("API_KEY_FOR_SuperJet")
        headers = {'X-Api-App-Id': sj_api_key}
        param = {'keyword': search, 'count': 50}

        request = requests.get(self.url, headers=headers, params=param)
        data = request.json()['objects']

        vacancies = []

        for item in data:
            vacancy = {
                'name': item['profession'], 'url': item['link'], 'employment': item['type_of_work']['title'], 'experience': item['experience']['title']
            }
            if item['payment_from'] == item['payment_to'] == 0:
                vacancy['min_salary'] = 'По результатам собеседования'
                vacancy['max_salary'] = 'По результатам собеседования'
                vacancy['currency'] = 'Значение не указано'
            else:
                if item['payment_from'] == 0:
                    vacancy['min_salary'] = 'Минимальная зарплата не указана'
                    vacancy['currency'] = 'Не указано'
                else:
                    vacancy['min_salary'] = item['payment_from']
                    vacancy['currency'] = item['currency']

                if item['payment_to'] == 0:
                    vacancy['max_salary'] = 'Максимальная зарплата не указана'
                else:
                    vacancy['max_salary'] = item['payment_to']
                    vacancy['currency'] = item['currency']

            vacancies.append(vacancy)

        return vacancies


