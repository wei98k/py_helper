import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 抖音平台特定配置
DOUYIN_CONFIG = {
    # 用户主页相关配置
    'USER_PAGE': {
        'SCROLL_INTERVAL': float(os.getenv('DOUYIN_USER_SCROLL_INTERVAL', 1.5)),
        'MAX_RETRY': int(os.getenv('DOUYIN_USER_MAX_RETRY', 3)),
        'VIDEO_CSS_SELECTOR': os.getenv('DOUYIN_VIDEO_SELECTOR', '.Eie04v01')
    },
    
    # 搜索页面相关配置
    'SEARCH_PAGE': {
        'SCROLL_INTERVAL': float(os.getenv('DOUYIN_SEARCH_SCROLL_INTERVAL', 2.0)),
        'MAX_RETRY': int(os.getenv('DOUYIN_SEARCH_MAX_RETRY', 5)),
        'SORT_TYPES': {
            'general': '',
            'hot': '&sort_type=2',
            'newest': '&sort_type=3'
        }
    },
    
    # 详情页面相关配置
    'DETAIL_PAGE': {
        'LOAD_WAIT_TIME': float(os.getenv('DOUYIN_DETAIL_LOAD_WAIT', 3.0)),
        'INFO_SELECTORS': {
            'title': '.XePDue01',
            'author_name': '.Vfpdue01',
            'author_id': '.Vfpdue01 + a',
            'stats': '.Eie04v01 .eX4lA001',
            'description': '.webcast-chatroom___description',
            'cover': '.DouyinVideoPlayer video',
            'tags': '.text-tag'
        }
    },
    
    # API相关配置
    'API': {
        'VIDEO_URL_TEMPLATE': os.getenv('DOUYIN_VIDEO_URL_TEMPLATE', 'https://example.com/video/{video_id}.mp4'),
        'USER_AGENT': os.getenv('DOUYIN_USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')
    }
}

# 导出配置
def get_douyin_config():
    return DOUYIN_CONFIG