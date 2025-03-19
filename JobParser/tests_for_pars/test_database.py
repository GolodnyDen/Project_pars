import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Добавляем корневую директорию проекта в PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')

from ParsPart.app.database import insert_jobs  # Используйте правильный путь

class TestDatabase(unittest.TestCase):
    @patch('ParsPart.app.database.get_db')  # Мокируем функцию get_db
    def test_insert_jobs(self, mock_get_db):
        # Создаем мок для соединения с базой данных
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_db.return_value = mock_conn

        # Вставляем тестовые данные
        jobs = [
            ("Python Developer", "IT Company", "100 000 руб.", "2 года", "Москва"),
            ("Java Developer", "Tech Corp", "150 000 руб.", "3 года", "Санкт-Петербург")
        ]
        insert_jobs(jobs)

        # Проверяем, что метод executemany был вызван с правильными данными
        mock_cursor.executemany.assert_called_once_with(
            """
            INSERT INTO jobs (title, company, salary, experience, city) 
            VALUES (%s, %s, %s, %s, %s)
            """,
            jobs
        )
        mock_conn.commit.assert_called_once()

    @patch('ParsPart.app.database.get_db')  # Мокируем функцию get_db
    def test_insert_empty_jobs(self, mock_get_db):
        # Создаем мок для соединения с базой данных
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_db.return_value = mock_conn

        # Вставляем пустой список
        insert_jobs([])

        # Проверяем, что метод executemany не был вызван
        mock_cursor.executemany.assert_not_called()
        mock_conn.commit.assert_not_called()

if __name__ == '__main__':
    unittest.main()