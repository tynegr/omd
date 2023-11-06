import urllib.request
import json
import unittest
from unittest.mock import patch

API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


class TestWhatIsYearNow(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_DMY(self, mock_urlopen):
        mock_response = {'currentDateTime': '06.11.2023'}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            json.dumps(mock_response).encode('utf-8')

        year = what_is_year_now()
        self.assertEqual(year, 2023)

    @patch('urllib.request.urlopen')
    def test_YMD(self, mock_urlopen):
        mock_response = {'currentDateTime': '2023-11-06'}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            json.dumps(mock_response).encode('utf-8')

        year = what_is_year_now()
        self.assertEqual(year, 2023)
        
    @patch('urllib.request.urlopen')
    def test_inappropriate_format(self, mock_urlopen):
        mock_response = {'currentDateTime': '2023/11/06'}
        mock_urlopen.return_value.__enter__.return_value.read.return_value \
            = json.dumps(mock_response).encode('utf-8')

        with self.assertRaises(ValueError):
            what_is_year_now()

    @patch('urllib.request.urlopen')
    def test_missing_year(self, mock_urlopen):
        mock_response = {'currentDateTime': '11-06'}
        mock_urlopen.return_value.__enter__.return_value.read.return_value \
            = json.dumps(mock_response).encode('utf-8')

        with self.assertRaises(IndexError):
            what_is_year_now()

    @patch('urllib.request.urlopen')
    def test_missing_datetime(self, mock_urlopen):
        mock_response = {'noDatetime': 'invalid'}
        mock_urlopen.return_value.__enter__.return_value.read.return_value \
            = json.dumps(mock_response).encode('utf-8')

        with self.assertRaises(KeyError):
            what_is_year_now()


if __name__ == '__main__':
    unittest.main()
    
