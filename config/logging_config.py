# config/logging_config.py
import logging
import os

# 设置日志文件路径
log_dir = "logs"
log_file = os.path.join(log_dir, "stock_value_scoring_system.log")

# 确保 logs 文件夹存在
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),  # 写入文件
        logging.StreamHandler()  # 输出到控制台
    ]
)

logger = logging.getLogger(__name__)
logger.info("日志配置加载成功，文件和控制台输出均已配置。")
