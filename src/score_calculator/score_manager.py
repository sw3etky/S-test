# src/score_calculator/score_manager.py

from src.data_fetcher.financial_data_fetcher import fetch_financial_data
from .score_rules import pe_ratio_score, roe_score

def calculate_stock_score(stock_code: str) -> int:
    """获取财务数据并计算股票总评分。"""
    data = fetch_financial_data(stock_code)
    
    if not data:
        return 0  # 如果没有获取到数据，返回0分
    
    pe_score = pe_ratio_score(data["pe_ratio"])
    roe_score_val = roe_score(data["roe"])
    
    total_score = pe_score + roe_score_val
    return total_score
