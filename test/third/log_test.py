import logging
import unittest


class LogTest(unittest.TestCase):
    def setUp(self) -> None:
        LOG_FORMAT = '%(asctime)s - %(levelname)s - %(filename)s/%(funcName)s(%(lineno)s) - %(message)s'
        DATE_FORMAT = "%Y-%m-%d %H:%M:%S"  # 日期格式
        self.file = "out.log"
        fp = logging.FileHandler(self.file, encoding='utf-8')
        fs = logging.StreamHandler()
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])  # 调用

    def tearDown(self) -> None:
        # os.remove(self.file)
        pass

    def test_log(self):
        logging.debug("This is a debug log.哈哈")
        logging.info("This is a info log.")
        logging.warning("This is a warning log.")
        logging.error("This is a error log.")
        logging.critical("This is a critical log.")
