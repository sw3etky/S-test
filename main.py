# src/main.py

from src.data_fetcher.stock_list_fetcher import fetch_stock_list
from src.score_calculator.score_manager import calculate_stock_score
from src.visualizer.visualization_tools import plot_stock_scores
from config.logging_config import logger

def main():
    # 获取股票列表
    stock_list = fetch_stock_list()
    if stock_list.empty:
        logger.error("股票列表为空，程序退出。")
        return

    stock_scores = []
    # 假设股票列表 DataFrame 中字段名为 "代码" 和 "名称"
    for _, row in stock_list.iterrows():
        stock_code = row["代码"]
        score = calculate_stock_score(stock_code)
        stock_scores.append({"stock_code": stock_code, "score": score})
    
    # 输出评分结果到控制台
    for s in stock_scores:
        print(f"股票 {s['stock_code']} 的评分为: {s['score']}")
    
    # 调用可视化函数展示评分结果
    plot_stock_scores(stock_scores)

if __name__ == "__main__":
    main()
