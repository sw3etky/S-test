# src/utils/fetch_data.py

import akshare as ak

def fetch_stock_data(stock_code: str):
    """
    获取某只股票的数据，假设我们使用 akshare 库来获取。
    :param stock_code: 股票代码
    :return: 股票数据
    """
    try:
        stock_data = ak.stock_zh_a_hist(symbol=stock_code, period='daily', adjust='qfq')
        return stock_data
    except Exception as e:
        print(f"获取股票数据失败: {e}")
        return None
