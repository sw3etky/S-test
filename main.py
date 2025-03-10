# src/main.py

from src.data_fetcher.stock_fetch_list import stock_fetch_list
from src.score_calculator.score_manager import calculate_stock_score
from src.visualizer.visualization_tools import plot_stock_scores
from config.logging_config import logger

def main():
    stock_list = stock_fetch_list()
    if stock_list.empty:
        logger.error("股票列表为空，程序退出。")
        return

    stock_scores = []
    # 假设股票列表中列名为 "code" 和 "name"
    for _, row in stock_list.iterrows():
        stock_code = row.get("code") or row.get("代码")
        if not stock_code:
            logger.warning("未找到股票代码")
            continue
        score = calculate_stock_score(stock_code)
        stock_scores.append({"stock_code": stock_code, "score": score})
    
    for s in stock_scores:
        print(f"股票 {s['stock_code']} 的评分为: {s['score']}")
    
    plot_stock_scores(stock_scores)

if __name__ == "__main__":
    main()
