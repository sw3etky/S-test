# src/data_fetcher/financial_data_fetcher.py

import akshare as ak
import pandas as pd
from config.logging_config import logger

def fetch_financial_data(stock_code: str) -> dict:
    """
    获取单支股票的财务数据（例如市盈率和净资产收益率）。
    
    Args:
        stock_code (str): 股票代码
    
    Returns:
        dict: 包含 'pe_ratio' 和 'roe' 的数据字典，若获取失败返回空字典。
    """
    try:
        # 使用 akshare 获取财务指标数据
        financial_df = ak.stock_financial_analysis_indicator(stock=stock_code)
        if financial_df.empty:
            logger.warning(f"{stock_code} 的财务数据为空")
            return {}
        latest = financial_df.iloc[-1]
        pe_ratio = latest.get("市盈率", None)
        roe = latest.get("净资产收益率", None)
        logger.info(f"获取 {stock_code} 财务数据成功: PE={pe_ratio}, ROE={roe}")
        return {"pe_ratio": pe_ratio, "roe": roe}
    except Exception as e:
        logger.error(f"获取 {stock_code} 财务数据失败: {e}")
        return {}

if __name__ == "__main__":
    data = fetch_financial_data("000001")
    print(data)
