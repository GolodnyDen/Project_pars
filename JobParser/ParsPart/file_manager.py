def save_to_txt(jobs):
    try:
        with open("vacancies.txt", "a", encoding="utf-8") as file:
            for job in jobs:
                file.write(f"Название: {job['title']}\n")
                file.write(f"Компания: {job['company']}\n")
                file.write(f"Зарплата: {job['salary']}\n")
                file.write(f"Опыт: {job['experience']}\n")
                file.write(f"Город: {job['city']}\n")
                file.write("---\n\n")
    except Exception as e:
        print(f"Ошибка записи в файл: {e}")

def read_from_txt():
    try:
        with open("vacancies.txt", "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Файл с вакансиями еще не создан."
    except Exception as e:
        return f"Ошибка чтения файла: {e}"