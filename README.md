# dp_helper

## 功能

dp采集助手，使用Drissionpage实现多平台数据采集，当前支持抖音平台，包括:
- 用户主页全部视频采集
- 搜索页视频采集
- 视频详情页数据采集

## 环境依赖

- Python 3.8+
- Drissionpage
- requests
- tqdm
- ffmpeg
- python-dotenv

## 部署运行

```
python job:run --listen
python api:run
python spider:run 
python 
```

## 项目结构
```
dp_helper/
├── config/                 # 配置文件目录
│   ├── settings.py         # 全局设置
│   └── douyin_config.py    # 抖音平台配置
├── core/                   # 核心功能模块
│   ├── douyin/
│   │   ├── user_parser.py  # 用户主页解析器
│   │   ├── search_parser.py # 搜索页解析器
│   │   └── detail_parser.py # 详情页解析器
│   └── base_parser.py      # 基础解析器类
├── storage/                # 数据存储目录
│   └── douyin/
│       ├── videos/         # 视频文件存储
│       ├── covers/         # 封面图片存储
│       └── data/           # 元数据存储
├── utils/                  # 工具函数目录
│   ├── downloader.py       # 下载工具
│   └── logger.py           # 日志工具
├── examples/               # 使用示例
│   ├── douyin_user_example.py
│   ├── douyin_search_example.py
│   └── douyin_detail_example.py
├── requirements.txt        # 依赖包列表
└── README.md               # 项目说明文档
```

## 安装方法

```bash
# 克隆仓库
git clone <repository-url>
cd dp_helper

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑.env文件设置必要参数
```

## 使用示例

### 采集抖音用户主页视频
```python
from core.douyin.user_parser import DouyinUserParser

parser = DouyinUserParser()
parser.collect_user_videos(user_id="123456789")
```

### 搜索并采集视频
```python
from core.douyin.search_parser import DouyinSearchParser

parser = DouyinSearchParser()
parser.search_and_collect(keyword="美食", max_count=50)
```

## 配置说明

所有配置项位于config目录下，主要配置包括:
- 下载路径设置
- 请求频率控制
- 代理配置
- 日志级别

## 注意事项

1. 使用前请确保已安装ffmpeg并配置到环境变量
2. 频繁采集可能导致IP被限制，建议配置代理池
3. 请遵守各平台robots协议和使用条款
4. 本工具仅供学习研究使用，请勿用于商业用途





```
project_root/
├── app/                      # 核心应用代码
│   ├── console/              # 命令行程序
│   │   └── commands/        # Artisan风格命令
│   ├── daemons/              # 持续运行服务 ★核心新增★
│   │   ├── kafkaListener/   # Kafka消费服务
│   │   │   ├── Consumer.py  # 消费逻辑
│   │   │   ├── Manager.py   # 进程管理
│   │   │   └── Workers/     # 子进程实现
│   │   └── SocketServer/    # 其他长连接服务
│   ├── Events/              # 事件定义
│   ├── Exceptions/          # 自定义异常
│   ├── Http/                # 接口层
│   │   ├── Controllers/
│   │   ├── Middleware/
│   │   └── Requests/
│   ├── Jobs/                # 可队列化任务
│   │   ├── Periodic/       # 周期任务
│   │   └── OneTime/        # 一次性任务
│   ├── Listeners/          # 事件监听器
│   ├── Models/             # 数据模型
│   │   ├── Mongo/
│   │   └── Sql/
│   ├── Providers/          # 服务提供者(DI)
│   └── Services/           # 业务服务
│       ├── Crawler/
│       └── Analytics/
├── bootstrap/              # 启动配置
│   ├── app.py              # 应用初始化
│   └── providers.py        # 依赖注册
├── config/                 # 配置文件
│   ├── daemons.py          # 守护进程配置 ★新增★
│   ├── database.py
│   └── kafka.py
├── database/
│   ├── migrations/
│   └── seeders/
├── public/                 # 对外入口
├── resources/
│   └── views/
├── routes/
│   ├── api.py
│   └── console.py         # 命令行路由
├── storage/
│   ├── logs/              # 按服务分日志 ★强化★
│   │   ├── daemons/
│   │   │   ├── kafka/
│   │   │   └── socket/
│   │   └── tasks/
│   └── cache/
├── supervisor/            # 进程管理 ★新增★
│   ├── kafka.ini
│   └── socket_server.ini
├── tests/
│   ├── Unit/
│   └── Feature/
├── venv/
├── artisan.py             # 命令行入口
└── requirements/
    ├── daemons.txt        # 守护进程依赖 ★新增★
    └── services.txt 
```