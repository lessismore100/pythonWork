"""
    关于open()的mode参数：
    'r'：读
    'w'：写
    'a'：追加
    'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
    'w+' == w+r（可读可写，文件若不存在就创建）
    'a+' ==a+r（可追加可写，文件若不存在就创建）
    对应的如果是二进制文件，就都加一个b就好啦：
    'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'
"""


class FileUtil:

    def __init__(self, path, result):
        self.path = path
        self.result = result

    def write_content(self):
        result_path = self.path + 'result.txt'
        fp_result = open(result_path, 'a+')  # mode:append
        fp_result.write(self.result)
