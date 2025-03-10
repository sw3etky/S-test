# src/data_fetcher/stock_list_fetcher.py

import os
import time
import pandas as pd
import akshare as ak
from config.logging_config import logger
from config.config import CACHE_PATH, CACHE_EXPIRATION

CACHE_FILE = os.path.join(CACHE_PATH, "stock_list.csv")

def fetch_stock_list() -> pd.DataFrame:
    """
    获取所有A股股票的代码和名称。
    如果缓存存在且未过期，则从缓存加载；否则从 akshare 获取并缓存。
    """
    if os.path.exists(CACHE_FILE) and (time.time() - os.path.getmtime(CACHE_FILE) < CACHE_EXPIRATION):
        logger.info("从缓存加载股票列表")
        return pd.read_csv(CACHE_FILE)
    
    logger.info("从 akshare 获取股票列表")
    try:
        stock_list = ak.stock_info_a_code_name()
        os.makedirs(CACHE_PATH, exist_ok=True)
        stock_list.to_csv(CACHE_FILE, index=False)
        logger.info("股票列表缓存成功")
        return stock_list
    except Exception as e:
        logger.error(f"获取股票列表失败: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    df = fetch_stock_list()
    print(df.head())
