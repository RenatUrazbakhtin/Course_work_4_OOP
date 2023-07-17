import json

from src.api_class import HeadHunter, SuperJob
from src.add_vacancies_class import JsonSaverVacancy
from src.vacancies_class import Vacancy

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

def save_to_json(search: str, platform):

    saved_data = JsonSaverVacancy()

    return saved_data.add_vacancy_to_file(search_vacancies(search, platform)), saved_data

def interaction_func():
    print("Здравствуйте, данная программа предназначена для поиска вакансий")

    while True:
        platform = int(input("Выберите платформу, на которой ищете вакансии (1 - HH.ru, 2 - SuperJob, 3 - Обе) \n"))
        if int(platform) == 1 or int(platform) == 2 or int(platform) == 3:
            break
        else:
            print("Введите номер существующей платформы(1, 2, 3) \n")

    search = str(input("Введите ключевое слово для поиска \n"))

    print("Подобранные вакансии расположены в файле 'search.json'")
    vacancies = save_to_json(search, platform)
    atribute_jsonsaver = save_to_json(search, platform)[1]
    copy_atribute_jsonsaver = atribute_jsonsaver
    for i in range(1000):
        do_u_want_filter = input("Вы хотите применить фильтры к поиску?(Да/Нет)\n")
        if do_u_want_filter.lower() == "нет" or do_u_want_filter.lower() == "no":
            print("Как хотите:(\n")
            break
        elif do_u_want_filter.lower() == "да" or do_u_want_filter.lower() == "yes":
            user_answer = int(input("Выберите желаемую фильтрацию (1 - Уровень средней ЗП, 2 - ЗП от, 3 - ЗП до, 4 - Валюта ЗП, 5 - Опыт работы)\n"))

            if user_answer == 1:
                while True:
                    user_average_salary = int(input("Введите желаемый уровень средней ЗП\n"))
                    if type(user_average_salary) != int:
                        print("Пожалуйста, введите числовое значение")
                    else:
                        break
                if i == 0:
                    vacancy_by_average_salary = atribute_jsonsaver.get_vacancy_by_salary_average(user_average_salary, search_vacancies(search, platform))
                    if vacancy_by_average_salary == []:
                        print("Вакансий с подобным фильтром не найдено")
                    print(json.dumps(vacancy_by_average_salary, indent=2, ensure_ascii=False))
                else:
                    vacancy_by_average_salary = atribute_jsonsaver.get_vacancy_by_salary_average(user_average_salary, search_vacancies(search, platform))
                    copy_vacancy_average = atribute_jsonsaver.get_vacancy_by_salary_average(user_average_salary, vacancy_by_average_salary)
                    if copy_vacancy_average == []:
                        print("С подобными фильтрами вакансий не найдено")
                    else:
                        print(json.dumps(copy_vacancy_average, indent=2, ensure_ascii=False))


            if user_answer == 2:
                while True:
                    user_salary_from = int(input("Введите уровень ЗП от\n"))
                    if type(user_salary_from) != int:
                        print("Пожалуйста, введите числовое значение")
                    else:
                        break
                if i == 0:
                    vacancy_by_salary_from = atribute_jsonsaver.get_vacancy_by_salary_from(user_salary_from, search_vacancies(search, platform))
                    if vacancy_by_salary_from == []:
                        print("Вакансий с подобным фильтром не найдено")
                    print(json.dumps(vacancy_by_salary_from, indent=2, ensure_ascii=False))
                else:
                    vacancy_by_salary_from = atribute_jsonsaver.get_vacancy_by_salary_from(user_salary_from, search_vacancies(search, platform))
                    copy_vacancy_by_salary_from = atribute_jsonsaver.get_vacancy_by_salary_from(user_salary_from, vacancy_by_salary_from)
                    if copy_vacancy_by_salary_from == []:
                        print("С подобными фильтрами вакансий не найдено")
                    else:
                        print(json.dumps(copy_vacancy_by_salary_from, indent=2, ensure_ascii=False))

            if user_answer == 3:
                while True:
                    user_salary_to = int(input("Введите уровень ЗП до\n"))
                    if type(user_salary_to) != int:
                        print("Пожалуйста, введите числовое значение")
                    else:
                        break
                if i == 0:
                    vacancy_by_salary_to = atribute_jsonsaver.get_vacancy_by_salary_to(user_salary_to, search_vacancies(search, platform))
                    if vacancy_by_salary_to == []:
                        print("Вакансий с подобным фильтром не найдено")
                    print(json.dumps(vacancy_by_salary_to, indent=2, ensure_ascii=False))
                else:
                    vacancy_by_salary_to = atribute_jsonsaver.get_vacancy_by_salary_to(user_salary_to, search_vacancies(search, platform))
                    copy_vacancy_by_salary_to = atribute_jsonsaver.get_vacancy_by_salary_to(user_salary_to, vacancy_by_salary_to)
                    if copy_vacancy_by_salary_to == []:
                        print("С подобными фильтрами вакансий не найдено")
                    else:
                        print(json.dumps(copy_vacancy_by_salary_to, indent=2, ensure_ascii=False))

            if user_answer == 4:
                while True:
                    user_salary_currency = input("Введите валюту ЗП\n")
                    if type(user_salary_currency) != str:
                        print("Пожалуйста, введите буквенное значение")
                    else:
                        break
                if i == 0:
                    vacancy_by_currency = atribute_jsonsaver.get_vacancy_by_currency(user_salary_currency, search_vacancies(search, platform))
                    if vacancy_by_currency == []:
                        print("Вакансий с подобным фильтром не найдено")
                    print(json.dumps(vacancy_by_currency, indent=2, ensure_ascii=False))
                else:
                    vacancy_by_currency = atribute_jsonsaver.get_vacancy_by_currency(user_salary_currency, search_vacancies(search, platform))
                    copy_vacancy_by_currency = atribute_jsonsaver.get_vacancy_by_currency(user_salary_currency, vacancy_by_currency)
                    if copy_vacancy_by_currency == []:
                        print("С подобными фильтрами вакансий не найдено")
                    else:
                        print(json.dumps(copy_vacancy_by_currency, indent=2, ensure_ascii=False))

            if user_answer == 5:
                while True:
                    user_experience = input("Введите опыт работы(без опыта, от 1 года, от 3 лет, от 6 лет)\n")
                    if str(user_experience) != "без опыта" and str(user_experience) != "от 1 года" and str(user_experience) != "от 3 лет" and str(user_experience) != "от 6 лет":
                        print("Пожалуйста, введите корректное значение")
                    else:
                        break
                if i == 0:
                    vacancy_by_experience = atribute_jsonsaver.get_vacancy_by_experience(user_experience, search_vacancies(search, platform))
                    if vacancy_by_experience == []:
                        print("Вакансий с подобным фильтром не найдено")
                    print(json.dumps(vacancy_by_experience, indent=2, ensure_ascii=False))
                else:
                    vacancy_by_experience = atribute_jsonsaver.get_vacancy_by_experience(user_experience, search_vacancies(search, platform))
                    copy_vacancy_by_experience = atribute_jsonsaver.get_vacancy_by_experience(user_experience, vacancy_by_experience)
                    if copy_vacancy_by_experience == []:
                        print("С подобными фильтрами вакансий не найдено")
                    else:
                        print(json.dumps(copy_vacancy_by_experience, indent=2, ensure_ascii=False))

