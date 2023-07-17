
class Vacancy:
    """
    Класс для работы с вакансиями и их записи в читаемый вид
    """
    def __init__(self, vacancy_dict: dict):
        self.vacancy_name = vacancy_dict["name"]
        self.vacancy_url = vacancy_dict["url"]
        self.min_salary = vacancy_dict["min_salary"]
        self.max_salary = vacancy_dict["max_salary"]
        self.currency = vacancy_dict["currency"]
        self.employment = vacancy_dict["employment"]
        self.experience = vacancy_dict["experience"]
        if type(vacancy_dict["min_salary"]) == str and type(vacancy_dict["max_salary"]) == str:
            self.average_salary = 0
        elif type(vacancy_dict["min_salary"]) == str:
            self.average_salary = self.max_salary
        elif type(vacancy_dict["max_salary"]) == str:
            self.average_salary = self.min_salary
        else:
            self.average_salary = round((self.max_salary + self.min_salary)/2)

    def __le__(self, other):
        if self.average_salary <= other.average_salary:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.average_salary >= other.average_salary:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.average_salary < other.average_salary:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.average_salary > other.average_salary:
            return True
        else:
            return False

    def create_dict(self):
        """
        Создания читаемого для пользователя списка словарей с вакансиями
        :return: список словарей
        """
        dictionary = {
            "Ваканcия": self.vacancy_name,
            "Ссылка": self.vacancy_url,
            "Опыт работы": self.experience,
            "Занятость": self.employment,
            "ЗП": {
                "От": self.min_salary,
                "До": self.max_salary,
                "Средняя ЗП": self.average_salary,
                "Валюта": self.currency
            }
        }
        return dictionary




