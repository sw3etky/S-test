# tests/test_data_fetcher.py

import unittest
from src.data_fetcher.stock_list_fetcher import fetch_stock_list

class TestDataFetcher(unittest.TestCase):
    def test_fetch_stock_list(self):
        df = fetch_stock_list()
        self.assertFalse(df.empty, "股票列表为空，测试失败")

if __name__ == '__main__':
    unittest.main()
