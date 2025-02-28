# src/data_fetcher/stock_fetch_list.py
import sys
import os
import time
import pandas as pd
import akshare as ak

# 获取项目根目录并添加到 sys.path 中
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.logging_config import logger

# 缓存文件路径和过期时间设置
CACHE_FILE = "data/cache/stock_list.csv"
CACHE_EXPIRATION = 86400  # 24小时

def fetch_stock_list() -> pd.DataFrame:
    logger.info("Starting fetch_stock_list function.")
    
    """
    获取所有A股股票的代码和名称。
    如果缓存存在且未过期，则从缓存中加载；否则重新获取并更新缓存。
    """

    # 检查缓存文件是否存在且在有效期内
    if os.path.exists(CACHE_FILE):
        cache_age = time.time() - os.path.getmtime(CACHE_FILE)
        logger.info(f"Cache file age: {cache_age} seconds.")
        if cache_age < CACHE_EXPIRATION:
            logger.info("Loading stock list from cache.")
            return pd.read_csv(CACHE_FILE)

    logger.info("Cache expired or not found, fetching new data.")

    # 获取新数据
    try:
        stock_list = ak.stock_info_a_code_name()
        logger.info("Data fetched from akshare.")

        if not stock_list.empty:
            os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
            stock_list.to_csv(CACHE_FILE, index=False)
            logger.info("成功获取所有A股股票代码和名称，并保存到缓存。")
        else:
            logger.warning("Fetched stock list is empty.")
        return stock_list
    except Exception as e:
        logger.error(f"获取股票列表失败: {e}")
        return pd.DataFrame()

# 确保函数在执行时运行
if __name__ == "__main__":
    stock_list = fetch_stock_list()
    if stock_list.empty:
        logger.warning("No stock data was retrieved.")
    else:
        logger.info("Stock data retrieved successfully.")