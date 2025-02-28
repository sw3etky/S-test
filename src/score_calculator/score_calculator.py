# src/score_calculator.py
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import fetch_data  # 假设你已经有一个获取股票数据的工具

# 获取项目根目录并添加到 sys.path 中
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.logging_config import logger


def calculate_pe_score(pe_ratio: float) -> float:
    """计算市盈率的评分"""
    if pe_ratio < 10:
        return 100
    elif pe_ratio < 20:
        return 75
    elif pe_ratio < 30:
        return 50
    else:
        return 25

def calculate_roe_score(roe: float) -> float:
    """计算ROE的评分"""
    if roe > 20:
        return 100
    elif roe > 15:
        return 80
    elif roe > 10:
        return 60
    else:
        return 40

def calculate_turnover_score(turnover_rate: float) -> float:
    """计算换手率的评分"""
    if turnover_rate > 3:
        return 100
    elif turnover_rate > 2:
        return 80
    elif turnover_rate > 1:
        return 60
    else:
        return 40

def calculate_stock_score(stock_data: pd.Series) -> float:
    """计算一只股票的综合评分"""
    pe_score = calculate_pe_score(stock_data['PE'])
    roe_score = calculate_roe_score(stock_data['ROE'])
    turnover_score = calculate_turnover_score(stock_data['TurnoverRate'])

    # 按比例加权合成总分
    total_score = 0.4 * pe_score + 0.3 * roe_score + 0.3 * turnover_score
    logger.info(f"Stock {stock_data['StockCode']} score: {total_score}")
    return total_score

def score_all_stocks(stock_list: pd.DataFrame) -> pd.DataFrame:
    """对所有股票进行评分"""
    stock_list['Score'] = stock_list.apply(calculate_stock_score, axis=1)
    return stock_list

# 示例：假设我们从 stock_fetch_list.py 获取了股票数据
if __name__ == "__main__":
    # 从 fetch_stock_list 获取数据
    stock_list = stock_fetch_list()
    if not stock_list.empty:
        scored_stocks = score_all_stocks(stock_list)
        logger.info("Scored all stocks successfully.")
        print(scored_stocks[['StockCode', 'StockName', 'Score']])
