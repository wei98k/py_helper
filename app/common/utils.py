def read_file(file_path, encoding='utf-8'):
    """
    封装一个读取文件的函数
    
    参数:
        file_path (str): 文件的路径
        encoding (str): 文件的编码格式，默认为 utf-8
    
    返回:
        str: 文件内容，如果读取失败则返回空字符串
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    except Exception as e:
        print(f"读取文件 {file_path} 时出错: {e}")
        return ''

def write_file(file_path, content, encoding='utf-8'):
    """
    封装一个写入文件的函数
    
    参数:
        file_path (str): 文件的路径
        content (str): 要写入的内容
        encoding (str): 文件的编码格式，默认为 utf-8
    
    返回:
        bool: 写入成功返回 True，失败返回 False
    """
    try:
        with open(file_path, 'w', encoding=encoding) as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"写入文件 {file_path} 时出错: {e}")
        return False

def append_file(file_path, content, encoding='utf-8'):
    """
    封装一个追加写入文件的函数
    
    参数:
        file_path (str): 文件的路径
        content (str): 要追加写入的内容
        encoding (str): 文件的编码格式，默认为 utf-8
    
    返回:
        bool: 追加写入成功返回 True，失败返回 False
    """
    try:
        with open(file_path, 'a', encoding=encoding) as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"追加写入文件 {file_path} 时出错: {e}")
        return False
