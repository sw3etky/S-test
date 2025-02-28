import akshare as ak
import pandas as pd
 
# 设置股票代码和时间范围
stock_code = "000001"  # 以上证指数为例
start_date = "20241101"
end_date = "20241114"
 
# 使用 akshare 获取股票 K 线数据
stock_data = ak.stock_zh_a_hist(symbol=stock_code, start_date=start_date, end_date=end_date, adjust="qfq")
 
print(stock_data)