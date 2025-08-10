import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 存储路径配置
STORAGE_PATH = {
    'videos': os.path.join(PROJECT_ROOT, 'storage/videos'),
    'covers': os.path.join(PROJECT_ROOT, 'storage/covers'),
    'data': os.path.join(PROJECT_ROOT, 'storage/data'),
    'response': os.path.join(PROJECT_ROOT, 'storage/response')
}

# 请求配置
REQUEST_CONFIG = {
    'timeout': int(os.getenv('REQUEST_TIMEOUT', 10)),
    'interval': float(os.getenv('REQUEST_INTERVAL', 1.0)),
    'user_agent': os.getenv('USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')
}

# 日志配置
LOG_CONFIG = {
    'level': os.getenv('LOG_LEVEL', 'INFO'),
    'file_path': os.path.join(PROJECT_ROOT, 'logs/app.log')
}

# 代理配置
PROXY_CONFIG = {
    'enable': os.getenv('PROXY_ENABLE', 'false').lower() == 'true',
    'http': os.getenv('PROXY_HTTP'),
    'https': os.getenv('PROXY_HTTPS')
}