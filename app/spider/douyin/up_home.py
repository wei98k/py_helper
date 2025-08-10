
from ast import main
import requests
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from config.settings import STORAGE_PATH

def parse_douyin_data(json_data):
    videos = json_data.get('aweme_list')
    for video in videos:
        print('视频ID', video.get('aweme_id'))
        print('视频标题', video.get('item_title'))
        print('视频描述', video.get('desc'))
        print('视频标签', video.get('caption'))
        print('发布时间', video.get('create_time'))
        print('视频地址',video.get('video').get('play_addr').get('url_list')[0])
        print('视频封面',video.get('video').get('cover').get('url_list')[1])

        video_count = video.get('statistics')
        if video_count:
            print('推荐数', video_count.get('recommend_count'))
            print('评论数', video_count.get('comment_count'))
            print('点赞数', video_count.get('digg_count'))
            # print('赞赏数', video_count.get('admire_count'))
            # print('播放数', video_count.get('play_count'))
            print('分享数', video_count.get('share_count'))
            print('收藏数', video_count.get('collect_count'))

        # https://www.douyin.com/user/MS4wLjABAAAAX3NNh1vNefo9PD0gEjkEx86Ar0On3a9TsgLSsZSxorA
        print('up主页', f'https://www.douyin.com/user/{video.get("author").get("sec_uid")}')
        print('up昵称', video.get('author').get('nickname'))
        print('up-uid', video.get('author').get('uid'))
        print('up-头像', video.get('author').get('avatar_thumb').get('url_list')[0])

        print('BGM-标题', video.get('music').get('title'))
        print('BGM-作者', video.get('music').get('author'))
        print('BGM-封面', video.get('music').get('cover_hd').get('url_list')[0])
        # print('BGM-地址', video.get('music').get('play_url').get('url_list')[0])


def download_video():
    """
    此函数用于下载抖音视频。
    这里简单模拟下载逻辑，实际应用中需要获取视频真实地址并进行下载操作。
    """
    # 模拟获取视频URL，实际应从 parse_douyin_data 等函数获取真实地址
    video_url = "https://example.com/video.mp4"
    try:
        response = requests.get(video_url, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        
        # 定义保存文件名
        filename = "downloaded_video.mp4"
        
        # 写入文件
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"视频下载成功，已保存为 {filename}")
    except requests.RequestException as e:
        print(f"视频下载失败: {e}")

def download_video():
    pass

def download_cover():
    pass

if __name__ == '__main__':
    print(STORAGE_PATH['response'])
    # parse_douyin_data()
