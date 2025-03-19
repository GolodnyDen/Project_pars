import requests
from bs4 import BeautifulSoup

class HHParser:
    def parse(self, job_title, city, company):
        jobs = []
        try:
            url = f'https://hh.ru/search/vacancy?text={job_title}&area={city}'
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Проверка статуса ответа
            soup = BeautifulSoup(response.text, 'html.parser')

            for item in soup.find_all('div', class_='vacancy-serp-item'):
                title_elem = item.find('a', class_='bloko-link')
                comp_elem = item.find('div', class_='vacancy-serp-item__meta-info-company')
                salary_elem = item.find('div', class_='vacancy-serp-item__sidebar')
                exp_elem = item.find('div', class_='vacancy-serp-item__info')
                location_elem = item.find('span', class_='vacancy-serp-item__meta-info')

                title = title_elem.text.strip() if title_elem else 'Не указано'
                comp = comp_elem.text.strip() if comp_elem else 'Не указано'
                salary = salary_elem.text.strip() if salary_elem else 'Не указано'
                exp = exp_elem.text.strip() if exp_elem else 'Опыт не указан'
                location = location_elem.text.strip() if location_elem else 'Не указано'

                if not company or company.lower() in comp.lower():
                    jobs.append({
                        'title': title,
                        'company': comp,
                        'salary': salary,
                        'experience': exp,
                        'city': location
                    })

        except requests.RequestException as e:
            print(f"Ошибка при запросе к HH.ru: {e}")

        return jobs

class AvitoParser:
    def parse(self, job_title, city, company):
        jobs = []
        try:
            url = f'https://www.avito.ru/moskva/rabota?q={job_title}&area={city}'
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Проверка статуса ответа
            soup = BeautifulSoup(response.text, 'html.parser')

            for item in soup.find_all('div', class_='iva-item-content'):
                title_elem = item.find('a', class_='link-link-MbQDP')
                comp_elem = item.find('div', class_='iva-item-text-Ge6dR')
                salary_elem = item.find('div', class_='price-price-E1Y7h')

                title = title_elem.text.strip() if title_elem else 'Не указано'
                comp = comp_elem.text.strip() if comp_elem else 'Не указано'
                salary = salary_elem.text.strip() if salary_elem else 'Не указано'
                exp = "Опыт не указан"
                location = city

                if not company or company.lower() in comp.lower():
                    jobs.append({
                        'title': title,
                        'company': comp,
                        'salary': salary,
                        'experience': exp,
                        'city': location
                    })

        except requests.RequestException as e:
            print(f"Ошибка при запросе к Avito: {e}")

        return jobs

class HabrCareerParser:
    def parse(self, job_title, city, company):
        jobs = []
        try:
            url = f'https://career.habr.com/vacancies?q={job_title}&area={city}'
            if city:
                url += f'&city_id={city}'
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Проверка статуса ответа
            soup = BeautifulSoup(response.text, 'html.parser')

            for item in soup.find_all('div', class_='vacancy-card__inner'):
                title_elem = item.find('a', class_='vacancy-card__title-link')
                comp_elem = item.find('a', class_='link-companies')
                salary_elem = item.find('div', class_='vacancy-card__salary')
                exp_elem = item.find('div', class_='vacancy-card__meta')

                title = title_elem.text.strip() if title_elem else 'Не указано'
                comp = comp_elem.text.strip() if comp_elem else 'Не указано'
                salary = salary_elem.text.strip() if salary_elem else 'Не указано'
                exp = exp_elem.text.strip() if exp_elem else 'Опыт не указан'
                location = city

                if not company or company.lower() in comp.lower():
                    jobs.append({
                        'title': title,
                        'company': comp,
                        'salary': salary,
                        'experience': exp,
                        'city': location
                    })

        except requests.RequestException as e:
            print(f"Ошибка при запросе к Habr Career: {e}")

        return jobs