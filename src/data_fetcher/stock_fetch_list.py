# src/data_fetcher/stock_list_fetcher.py

import os
import time
import sqlite3
import pandas as pd
import akshare as ak
from config.logging_config import logger
from config.config import DB_PATH, CACHE_EXPIRATION

def create_stock_list_table(conn):
    """创建股票列表表（如果不存在的话）"""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS stock_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stock_code TEXT UNIQUE NOT NULL,
        stock_name TEXT NOT NULL
    );
    """
    conn.execute(create_table_sql)
    conn.commit()

def save_stock_list_to_db(df: pd.DataFrame):
    """将 DataFrame 数据写入 SQLite 数据库的 stock_list 表中"""
    conn = sqlite3.connect(DB_PATH)
    create_stock_list_table(conn)
    # 使用 to_sql 保存数据，if_exists="replace" 意味着每次保存时都会覆盖旧数据
    df.to_sql("stock_list", conn, if_exists="replace", index=False)
    conn.close()
    logger.info("股票列表已保存到 SQLite 数据库")

def load_stock_list_from_db() -> pd.DataFrame:
    """从 SQLite 数据库加载股票列表"""
    if not os.path.exists(DB_PATH):
        logger.info("数据库文件不存在")
        return pd.DataFrame()
    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql_query("SELECT * FROM stock_list", conn)
        logger.info("从 SQLite 数据库加载股票列表")
    except Exception as e:
        logger.error(f"加载股票列表失败: {e}")
        df = pd.DataFrame()
    conn.close()
    return df

def is_db_cache_valid() -> bool:
    """
    判断数据库缓存是否有效。
    此处简单判断数据库文件的修改时间是否在缓存有效期内。
    """
    if os.path.exists(DB_PATH):
        age = time.time() - os.path.getmtime(DB_PATH)
        logger.info(f"数据库文件缓存年龄：{age}秒")
        return age < CACHE_EXPIRATION
    return False

def stock_fetch_list() -> pd.DataFrame:
    """
    获取所有 A 股股票的代码和名称：
    如果数据库缓存有效，则直接从数据库加载；
    否则，从 akshare 获取数据，并保存到数据库。
    """
    if is_db_cache_valid():
        df = load_stock_list_from_db()
        if not df.empty:
            return df

    # 缓存不存在或已过期，从 akshare 获取
    logger.info("从 akshare 获取股票列表")
    try:
        df = ak.stock_info_a_code_name()
        # 对 DataFrame 的列名进行检查，确保包含 "code" 和 "name" 列（根据实际情况调整）
        logger.info(f"股票列表预览：\n{df.head()}")
        save_stock_list_to_db(df)
        return df
    except Exception as e:
        logger.error(f"获取股票列表失败: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    df = stock_fetch_list()
    print(df.head())
