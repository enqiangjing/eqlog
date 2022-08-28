# eqlog 默认已初始化
from eqlog import eqlog, Logger

# 自定义初始化日志文件
log1 = Logger('test_a')
log2 = Logger('test_b', log_files_dir='./log/')


@log1.log
def test_log(test):
    print(test)


@eqlog.log
def test_log_func(test):
    print(test)
    eqlog.waring('test output waring!')
    log2.info(test + 'test test_b output')
    print(e)


if __name__ == '__main__':
    test_log('the function is test_log, file is test_log_three.py')
    test_log_func('the function is test_log_func, file is test_log_three.py')
