# src/score_calculator/score_manager.py

from src.data_fetcher.financial_data_fetcher import fetch_financial_data
from .score_rules import pe_ratio_score, roe_score
from config.logging_config import logger

def calculate_stock_score(stock_code: str) -> int:
    """
    获取指定股票的财务数据，并根据评分规则计算总分。
    """
    data = fetch_financial_data(stock_code)
    if not data:
        logger.warning(f"{stock_code} 没有财务数据，评分为 0")
        return 0
    pe = data.get("pe_ratio")
    roe = data.get("roe")
    total_score = pe_ratio_score(pe) + roe_score(roe)
    logger.info(f"{stock_code} 的评分为: {total_score}")
    return total_score

if __name__ == "__main__":
    score = calculate_stock_score("000001")
    print(f"000001 的评分: {score}")
