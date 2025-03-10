# src/visualizer/visualization_tools.py

import matplotlib.pyplot as plt

def plot_stock_scores(stock_scores: list):
    """
    根据股票评分数据生成条形图。
    
    参数:
        stock_scores: 列表，每个元素为字典，包含 "stock_code" 和 "score"。
    """
    codes = [item["stock_code"] for item in stock_scores]
    scores = [item["score"] for item in stock_scores]
    
    plt.figure(figsize=(10, 6))
    plt.bar(codes, scores, color='skyblue')
    plt.xlabel("股票代码")
    plt.ylabel("评分")
    plt.title("股票投资价值评分")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_data = [{"stock_code": "000001", "score": 18}, {"stock_code": "000002", "score": 16}]
    plot_stock_scores(test_data)
