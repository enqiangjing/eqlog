# eqlog 默认已初始化
from eqlog import eqlog, Logger

# 自定义初始化日志文件
log1 = Logger('test_a')
log2 = Logger('test_b')


@log1.log
def test_log(test):
    print('print', test)


@eqlog.log
def test_log_func(test):
    print('print', test)
    log2.info(test, '123', {'a': '1000'}, 1, 2.22222)
    print(e)


if __name__ == '__main__':
    test_log(test='the function is test_log, file is test_log.py')
    test_log_func('the function is test_log_func, file is test_log_one.py')
