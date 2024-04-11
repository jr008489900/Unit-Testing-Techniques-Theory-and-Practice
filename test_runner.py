import os
import pytest

def run_tests(directory):
    """
    在指定目錄下運行所有測試文件。

    Args:
        directory (str): 要遍歷的目錄路徑。

    Returns:
        None
    """
    filelist = []
    # 遍歷指定目錄下的所有文件和文件夾
    for root, dirs, files in os.walk(directory):
        # 遍歷當前目錄下的所有文件
        for file in files:
            # 如果文件以 '.py' 結尾且以 'test_' 開頭，則執行測試
            if file.endswith('.py') and file.startswith('test_'):
                # 構建測試文件的路徑
                test_file_path = os.path.join(root, file)
                # 執行測試文件
                print(test_file_path)
                filelist.append(test_file_path)
    pytest.main(filelist)
                

if __name__ == "__main__":
    # 指定要遍歷的目錄
    directory = './unittest'
    # 運行測試
    run_tests(directory)
