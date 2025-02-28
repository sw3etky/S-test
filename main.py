# src/main.py

from data_fetcher.stock_list_fetcher import fetch_stock_list
from score_calculator.score_manager import calculate_stock_score

def main():
    # 获取股票列表
    stock_list = fetch_stock_list()
    
    # 遍历股票并计算评分
    for _, row in stock_list.iterrows():
        stock_code = row["代码"]
        score = calculate_stock_score(stock_code)
        print(f"股票 {stock_code} 的评分为: {score}")

if __name__ == "__main__":
    main()
