import logging

logger = logging.getLogger('cnodeapp')
# 设置日志级别
logger.setLevel(logging.DEBUG)

# 格式
format = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s')

# logging文件处理器
fl = logging.FileHandler(filename='logs/cnode.log',mode='a',encoding='utf8')
# 设置fl的格式
fl.setFormatter(format)
# 打印命令行输出
sl = logging.StreamHandler()
# 设置sl的格式
sl.setFormatter(format)
# 加处理器
logger.addHandler(fl)
logger.addHandler(sl)

