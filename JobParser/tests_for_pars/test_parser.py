# tests/test_parser.py
import unittest
from unittest.mock import patch
from ParsPart.app.parser import HHParser
import sys
print("PYTHONPATH:", sys.path)

class TestHHParser(unittest.TestCase):
    @patch('requests.get')
    def test_parse_success(self, mock_get):

        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.text = '''
        <div class="vacancy-serp-item">
            <a class="bloko-link">Python Developer</a>
            <div class="vacancy-serp-item__meta-info-company">IT Company</div>
            <div class="vacancy-serp-item__sidebar">100 000 руб.</div>
            <div class="vacancy-serp-item__info">2 года</div>
            <span class="vacancy-serp-item__meta-info">Москва</span>
        </div>
        '''
        mock_get.return_value = mock_response

        parser = HHParser()
        jobs = parser.parse("Python", "Москва", "")
        self.assertEqual(len(jobs), 1)
        self.assertEqual(jobs[0]['title'], "Python Developer")
        self.assertEqual(jobs[0]['company'], "IT Company")
        self.assertEqual(jobs[0]['salary'], "100 000 руб.")

    @patch('requests.get')
    def test_parse_empty_response(self, mock_get):

        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.text = ''
        mock_get.return_value = mock_response

        parser = HHParser()
        jobs = parser.parse("Python", "Москва", "")
        self.assertEqual(len(jobs), 0)

    @patch('requests.get')
    def test_parse_request_exception(self, mock_get):

        mock_get.side_effect = Exception("Network error")

        parser = HHParser()
        jobs = parser.parse("Python", "Москва", "")
        self.assertEqual(len(jobs), 0)

if __name__ == '__main__':
    unittest.main()