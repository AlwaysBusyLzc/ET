# 根据扩展名删除文件
import os

# 配置扩展名列表
del_ext_list = ["meta"]


def del_by_ext(ext: str):
    """
    删除当前目录及子目录中所有指定扩展名的文件
    
    参数：
        ext (str): 扩展名
    """
    # 确保扩展名以点开头（避免用户输入类似 "txt" 的格式）
    if not ext.startswith("."):
        ext = "." + ext

    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(ext):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"已删除文件: {file_path}")
                except PermissionError:
                    print(f"权限不足，无法删除: {file_path}")
                except Exception as e:
                    print(f"删除失败 ({file_path}): {str(e)}")
    



if __name__ == "__main__":
    for ext in del_ext_list:
        del_by_ext(ext)
