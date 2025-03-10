# src/utils/helpers.py

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    对数据进行基本清洗，例如删除缺失值等。
    """
    return df.dropna()

if __name__ == "__main__":
    # 测试数据清洗函数
    df = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, None]})
    print("原始数据：")
    print(df)
    print("清洗后数据：")
    print(clean_data(df))
